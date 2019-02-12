if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='碧蓝航线绘图日记像素画生成工具')
    parser.add_argument('input', metavar='input', type=str, help='input file path')
    parser.add_argument('-o', '--output', type=str, help='output file path. image end by .png,video end by .avi')
    parser.add_argument('-m', '--mode', type=str, help='mode to run this program',
                        choices=["video", "image"], default="image")

    parser.add_argument('-b', '--bold', type=int, help='bold of lines of images,integer', default=0)
    parser.add_argument('-x', '--width', type=int, help='width to run', default=1)
    parser.add_argument('-y', '--height', type=int, help='height to run', default=1)
    parser.add_argument('-c', '--cutFrames', type=int,
                        help='extrace one frame in cutFrame(your input num) frames,mode video only', default=1)
    # parser.add_argument('-c', '--cutFrames', type=int, help='extrace one frame in cutFrame(your input num) frames,mode video only',default=1)
    args = parser.parse_args()

    if args.mode == "image":
        import paint

        # if args.x is None:
        #     args.x = 1
        # if args.y is None:
        #     args.y = 1
        print(f"start draw image {args.input}......")
        o = paint.drawN(imgPath=args.input, w=args.width, h=args.height, blur=args.bold)
        if not args.output is None:
            oPath = args.output

        else:
            import time

            oPath = f"azurlanePainting-{int(time.time())}.png"
        o.save(oPath, "PNG")
        print(f"image drawn completed -> {oPath}")
    elif args.mode == "video":
        import analyseVideo

        if not args.output is None:
            oPath = args.output

        else:
            import time

            oPath = f"azurlanePainting-{int(time.time())}.avi"
        print(f"start handdle video {args.input}......")
        analyseVideo.makeVideo(inputVideoPath=args.input, output=oPath,cutFrames=args.cutFrames, w=args.width, h=args.height,blur=args.bold)
        print(f"video handdled completed -> {oPath}")
