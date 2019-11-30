import os, re

pattern = re.compile("(.*).(jpg|jpeg|png|gif)")

def change_files(location):
    for i, fname in enumerate(os.listdir(location)):
        path = os.path.join(location, fname)
        if pattern.match(fname):
          try:
            ending=fname.split('.')[1]
            os.rename(path, os.path.join(location, f'{str(i)}.{ending}'))
            print(f'"{fname}" renamed to: "{str(i)}{ending}"')
          except Exception as e:
            print('Error: ' + str(e))

if __name__ == '__main__':
  change_files('./')
