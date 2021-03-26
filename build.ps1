# ----------------------------------- Setup ---------------------------------- #
$name = 'instawow-installer'

$dist = 'dist'
$path = "$dist/$name"
$zip  = "$name.zip"

sh clean.sh
mkdir $dist
# ---------------------------- Compile executable ---------------------------- #
python build.py --dist-dir="$path"
# ------------------------------- Archive files ------------------------------ #
Push-Location $dist
7z a -tzip $zip "$name/*"
Pop-Location
# ------------------------------------- - ------------------------------------ #
