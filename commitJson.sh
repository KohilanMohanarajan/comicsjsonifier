echo "Running script..."
python3 comicsjsonifier.py

echo "Copying this week to website..."
cp comicsweek_thisWeek.json ../mywebsite

echo "Copying next week to website..."
cp comicsweek_nextWeek.json ../mywebsite

cd ../mywebsite 

echo "Pulling from master..."
git pull

echo "Committing to master..."
git add comicsweek_thisWeek.json
git add comicsweek_nextWeek.json
git commit -m "Updated comics for this/next week"
git push
