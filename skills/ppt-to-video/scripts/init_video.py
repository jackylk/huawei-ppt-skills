#!/usr/bin/env python3
"""Create an offline Remotion starter without installing or overwriting files."""
import argparse,json,os
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('output',type=Path);p.add_argument('--runtime',type=Path)
a=p.parse_args();out=a.output.resolve()
if out.exists() and any(out.iterdir()):p.error('output must be absent or empty')
if a.runtime and not (a.runtime.resolve()/'node_modules').is_dir():p.error('runtime must contain node_modules')
(out/'src').mkdir(parents=True,exist_ok=True);(out/'public').mkdir()
(out/'package.json').write_text(json.dumps({'name':'ppt-video-project','private':True,'scripts':{'render':'remotion render src/index.jsx Intro output.mp4 --codec=h264'}},indent=2)+'\n')
if a.runtime:os.symlink(os.path.relpath(a.runtime.resolve()/'node_modules',out),out/'node_modules',target_is_directory=True)
(out/'src/timeline.json').write_text(json.dumps({'fps':30,'width':1920,'height':1080,'scenes':[{'id':'opening','durationFrames':360,'title':'请替换为业务问题','narration':None,'background':None,'captions':[]}]},ensure_ascii=False,indent=2)+'\n')
(out/'src/index.jsx').write_text('''import React from 'react';
import {registerRoot,Composition,AbsoluteFill,Sequence,Audio,Img,staticFile,useCurrentFrame,interpolate} from 'remotion';
import movie from './timeline.json';
const Scene=({scene})=>{const f=useCurrentFrame();const caption=scene.captions.find(c=>f>=c.from&&f<c.to);return <AbsoluteFill style={{background:'#071522',color:'#eef5fb',fontFamily:'sans-serif',justifyContent:'center',alignItems:'center'}}>{scene.background&&<Img src={staticFile(scene.background)} style={{position:'absolute',width:'100%',height:'100%',objectFit:'cover',opacity:.3}}/>}<div style={{fontSize:64,opacity:interpolate(f,[0,15],[0,1],{extrapolateRight:'clamp'})}}>{scene.title}</div>{scene.narration&&<Audio src={staticFile(scene.narration)}/>}<div style={{position:'absolute',bottom:70,fontSize:36}}>{caption?.text}</div></AbsoluteFill>};
const Video=()=>{let start=0;return <AbsoluteFill>{movie.scenes.map(scene=>{const from=start;start+=scene.durationFrames;return <Sequence key={scene.id} from={from} durationInFrames={scene.durationFrames}><Scene scene={scene}/></Sequence>})}</AbsoluteFill>};
registerRoot(()=> <Composition id="Intro" component={Video} fps={movie.fps} width={movie.width} height={movie.height} durationInFrames={movie.scenes.reduce((n,s)=>n+s.durationFrames,0)}/>);
''')
print(f'Created starter: {out}. Replace sample content, measure narration, design scenes, then render. No dependencies installed.')
