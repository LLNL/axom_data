# This Python script writes the heroic_roses.yaml file for Klee.

def write_yaml(f, shapes):
    f.write("dimensions: 2\n\nshapes:\n")

    for s in shapes:
        n = s["num"]
        for i in range(n):
            f.write(f"- name: {s['mat']}{i}\n")
            f.write(f"  material: {s['mat']}\n")
            f.write(f"  geometry:\n")
            f.write(f"    format: c2c\n")
            fn = s["file"]
            if "%d" in fn:
                fn = fn % i
            f.write(f"    path: ../contours/heroic_roses/c2c/{fn}\n")
            if s["dnr"]:
                lststr = str(s["dnr"]).replace("'",'"')
                f.write(f"  does_not_replace: {lststr}\n")

def main():
    shapes = ({"mat":"greenishbrown","num": 1, "file":"greenishbrown.contour", "dnr":[]},
          {"mat":"brightgreen","num": 1, "file":"brightgreen.contour", "dnr":["greenishbrown"]},
          {"mat":"darkgreen","num": 6, "file":"darkgreen%d.contour", "dnr":[]},
          {"mat":"blue","num": 7, "file":"blue%d.contour", "dnr":[]},
          {"mat":"yellow","num": 3, "file":"yellow%d.contour", "dnr":[]},
          {"mat":"purplish","num": 2, "file":"purplish%d.contour", "dnr":[]},
          {"mat":"pink","num": 2, "file":"pink%d.contour", "dnr":["darkgreen"]},
          {"mat":"black","num": 73, "file":"black%d.contour", "dnr":[]},
          {"mat":"red","num": 7, "file":"red%d.contour", "dnr":["black"]},
          {"mat":"brightgreen","num": 1, "file":"brightgreen_over.contour", "dnr":[]},
          {"mat":"darkgreen","num": 1, "file":"darkgreen_over1.contour", "dnr":[]}
	  )
    f = open("heroic_roses.yaml", "wt")
    write_yaml(f, shapes)
    f.close()

if __name__ == "__main__":
    main()
