import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import argparse

def convert(yoloFile, dims=(1104,800)):

	## Converting txt file

	x = []
	y = []

	readFile = open(yoloFile, 'r')

	lines = readFile.read().split('\n')

	for line in lines:

		if len(line) != 0:

			# vector in the YOLOv5 format: class x_center y_center width height confidence
			v = line.split(' ')

			# Inputs in YOLOv5 format
			inClass = v[0]
			inXC = float(v[1])
			inYC = float(v[2])
			inW = float(v[3])
			inH = float(v[4])
			inConf = float(v[5])

			# Outputs
			x.append(dims[0]*inXC)
			y.append(dims[1]*inYC)

	return [x, y]

def main(args):
	dims = (args.xdim, args.ydim)
	coords = convert(args.label, dims)

	im = plt.imread(args.image)
	implot = plt.imshow(im, cmap="gray")

	plt.scatter(x=coords[0], y=coords[1], color='r', s=1)
	plt.text(0.02, 0.01, "Defects Detected: "+str(len(coords[0])), fontsize=14, transform=plt.gcf().transFigure)

	print("Labeled image saved to: " + args.save)
	plt.savefig(args.save, dpi=args.dpi)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Reading info for main.')

	parser.add_argument('--label', action='store', nargs='?', type=str, default='demo_images/labels/r2_0200.txt', help='label output from YOLOv5.')
	parser.add_argument('--image', action='store', nargs='?', type=str, default='demo_images/r2_0200.tif', help='Original Image converted.')
	parser.add_argument('--xdim', action='store', nargs='?', type=int, default=1104, help='Width of image.')
	parser.add_argument('--ydim', action='store', nargs='?', type=int, default=800, help='Height of image.')
	parser.add_argument('--save', action='store', nargs='?', type=str, default='demo_images/r2_0200_labeled.png', help='Where to save output?')
	parser.add_argument('--dpi', action='store', nargs='?', type=int, default=200, help='Output dpi.')

	args = parser.parse_args()
	
	main(args)