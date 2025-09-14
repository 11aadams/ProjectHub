import os

projects_dir = "projects"
index_path = os.path.join(projects_dir, "index.md")

with open(index_path, "w") as f:
    f.write("# 📂 Project Index\n\n")
    f.write("This page lists all projects.\n\n---\n\n")

    for file in sorted(os.listdir(projects_dir)):
        if file == "index.md":
            continue
        if file.endswith((".html", ".md")):
            name = os.path.splitext(file)[0]
            f.write(f"- [{name}]({file})\n")

print("✅ Project index updated!")
