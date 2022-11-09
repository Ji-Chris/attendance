import argparse
import camera


parser = argparse.ArgumentParser("attendance")
subparsers = parser.add_subparsers(dest="command")
commands = {}
commands["setup"] = subparsers.add_parser("setup")
commands["start"] = subparsers.add_parser("start")


if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.command == "start":
        camera.main()
    elif args.command == "setup":
        camera.setup()
