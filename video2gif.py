#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, re, subprocess, click, imageio, glob
from skimage.transform import resize
from tqdm import tqdm
import os, subprocess, warnings
def output_shell(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, executable='/bin/bash'); stdout_output = p.stdout.read().decode(); p.stdout.close(); p.wait()
    return stdout_output

@click.command()
@click.option('--ofile', type=str, default='output_gif', help='The name of the output file.')
@click.option('--optimize', type=bool, default=True, help='If True, use gifsicle to compress the output.')
@click.option('--fps', type=int, default=-1, help='fps of gif')
@click.argument('directory', type=click.Path(exists=True), nargs=1)
def cli(directory, optimize, fps, ofile):
    '''
    Only jpg files please
    '''
    if fps == -1:
        return click.echo('please, give --fps parameter')

    # import pdb; pdb.set_trace();
    
    image_list = glob.glob(os.path.join(directory, '*jpg'))
    image_list = sorted(image_list, key = lambda x: int(os.path.basename(os.path.splitext(x)[0])))
    ofile_normal = os.path.join(directory, f'{ofile}.gif')
    ofile_optim = os.path.join(directory, f'{ofile}_optim.gif')

    with imageio.get_writer(ofile_normal, mode='I', fps=fps) as writer:
        for image in tqdm(image_list):
            im = imageio.imread(image)
            writer.append_data(im)

    output_shell('gifsicle --optimize {} --colors 256 -o {}'.format(ofile_normal, ofile_optim))



if __name__ == "__main__":
    cli()
