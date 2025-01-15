from django.shortcuts import render
from django.http import JsonResponse
import json

high_scores = []

def snake(request):
    return render(request, 'snake_game/snake.html')

def highscores(request):
    """Handle high score retrieval and updates."""
    global high_scores
    if request.method == 'POST':
        # Parse incoming score from request body
        try:
            data = json.loads(request.body)
            score = int(data.get('score', 0))
            if score > 0:
                # Add the score to the list and sort descending
                high_scores.append(score)
                high_scores = sorted(high_scores, reverse=True)[:5]  # Keep top 5 scores
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid score data'}, status=400)

    # Return high scores
    return JsonResponse({'high_scores': high_scores})
