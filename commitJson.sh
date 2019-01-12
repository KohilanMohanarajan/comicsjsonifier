echo "Running script..."
python3 comicsjsonifier.py

echo "Copying to website..."
cp comicsweek_thisWeek.json ../mywebsite
cd ../mywebsite 

echo "Pulling from master..."
git pull

echo "Committing to master..."
git add comicsweek_thisWeek.json
git commit -m "Updated comics for this week"
git push
