
def show_welcome():
    print("\n" + "=" * 48)
    print("                 CREATORFLOW")
    print("      Your Short-Form Content Assistant")
    print("=" * 48)


def show_menu():
    print("\nWhat do you need help with?")
    print("1. Create a video")
    print("2. Plan content")
    print("3. Analyze posts")
    print("4. Exit")


def ask_non_empty(prompt):
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("This field cannot be empty. Please try again.")


def create_video():
    print("\n--- IDEA-TO-STORY ASSISTANT ---")

    topic = ask_non_empty("Video topic: ")
    audience = ask_non_empty("Target audience: ")

    styles = ("educational", "funny", "storytelling")
    print("Available styles:", ", ".join(styles))

    while True:
        style = input("Choose a style: ").strip().lower()
        if style in styles:
            break
        print("Choose educational, funny, or storytelling.")

    if style == "educational":
        hook = f"Confused about {topic}? Let's break it down simply."
        example = f"Explain one key concept in {topic} with a beginner-friendly example."
    elif style == "funny":
        hook = f"When you try {topic} for the first time..."
        example = f"Show a relatable mistake beginners make with {topic}."
    else:
        hook = f"My journey learning {topic} started with one small step..."
        example = f"Tell a short story about learning or using {topic}."

    print("\n" + "=" * 48)
    print("YOUR VIDEO CONTENT PLAN")
    print("=" * 48)
    print(f"\nTopic: {topic}")
    print(f"Audience: {audience}")
    print(f"Style: {style.title()}")

    print("\n1. HOOK")
    print(hook)

    print("\n2. SCENE-BY-SCENE OUTLINE")
    print("Scene 1 (0-3 sec): Deliver the hook.")
    print(f"Scene 2 (3-10 sec): Introduce {topic} and why it matters.")
    print(f"Scene 3 (10-20 sec): {example}")
    print("Scene 4 (20-30 sec): Summarize one useful takeaway.")

    print("\n3. ON-SCREEN TEXT")
    print(f"{topic}: A simple guide")
    print("Key takeaway: Learn one step at a time.")

    print("\n4. CAPTION")
    print(
        f"Exploring {topic}? Save this video and share it "
        f"with someone in your audience: {audience}."
    )

    print("\n5. HASHTAGS")
    print("#LearnWithMe #ContentCreator #ShortFormVideo")

    print("\n6. CALL TO ACTION")
    print("Save this video and follow for more practical tips.")

    print("\n7. CREATOR TIP")
    print("Use readable text, clear visuals, and captions.")
    print(f"Choose examples that make sense for {audience}.")

    print("\nNote: Review topic-specific details before publishing.")


def plan_content():
    print("\n--- SMART CONTENT PLANNER ---")

    niche = ask_non_empty("Content niche: ")

    platforms = ("instagram", "youtube")
    print("Platforms:", ", ".join(platforms))

    while True:
        platform = input("Platform: ").strip().lower()
        if platform in platforms:
            break
        print("Please choose Instagram or YouTube.")

    goals = ("education", "growth", "engagement")
    print("Goals:", ", ".join(goals))

    while True:
        goal = input("Goal: ").strip().lower()
        if goal in goals:
            break
        print("Choose education, growth, or engagement.")

    while True:
        frequency = input("Videos per week (1-7): ").strip()
        if frequency.isdigit() and 1 <= int(frequency) <= 7:
            frequency = int(frequency)
            break
        print("Enter a whole number from 1 to 7.")

    ideas = [
        f"Introduce the basics of {niche}",
        f"Explain common mistakes in {niche}",
        f"Share three practical {niche} tips",
        f"Create a step-by-step {niche} tutorial",
        f"Answer a frequently asked {niche} question",
        f"Share a myth versus fact about {niche}",
        f"Summarize key lessons about {niche}"
    ]

    print("\n--- YOUR WEEKLY CONTENT PLAN ---")
    print(f"Niche: {niche}")
    print(f"Platform: {platform.title()}")
    print(f"Goal: {goal.title()}")
    print(f"Planned posts: {frequency}")

    for day in range(1, 8):
        if day <= frequency:
            print(f"\nDay {day}: {ideas[day - 1]}")
        else:
            print(f"\nDay {day}: Rest, reply to comments, or review metrics")

    if goal == "education":
        print("\nTip: Focus on clear explanations and useful examples.")
    elif goal == "growth":
        print("\nTip: Test different hooks and track audience retention.")
    else:
        print("\nTip: Ask relevant questions and invite thoughtful comments.")

    print("Treat this plan as a starting point; adapt it using results.")


def get_non_negative_integer(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number < 0:
                print("Please enter zero or a positive whole number.")
                continue
            return number
        except ValueError:
            print("Invalid number. Enter a whole number, such as 1200.")


def analyze_posts():
    print("\n--- PERFORMANCE DETECTIVE ---")

    views = get_non_negative_integer("Video views: ")
    if views == 0:
        print("Views must be greater than zero to calculate a rate.")
        return

    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")
    shares = get_non_negative_integer("Shares: ")

    interactions = likes + comments + shares
    engagement = interactions / views * 100

    print("\n--- YOUR VIDEO ANALYSIS ---")
    print(f"Views: {views}")
    print(f"Likes: {likes}")
    print(f"Comments: {comments}")
    print(f"Shares: {shares}")
    print(f"Total recorded interactions: {interactions}")
    print(f"Engagement rate: {engagement:.2f}%")

    if engagement < 2:
        print("Experiment: Test a clearer hook and a more relevant CTA.")
    elif engagement < 5:
        print("Experiment: Try a new format and invite specific feedback.")
    else:
        print("Experiment: Test similar topics and compare the results.")

    if interactions > views:
        print(
            "Note: Interactions can exceed views on some platforms or "
            "under different counting rules. Verify the source metrics."
        )

    print("This is a simple comparison metric, not proof of content quality.")
    print("Compare several posts before drawing conclusions.")


def main():
    show_welcome()

    while True:
        show_menu()
        choice = input("\nEnter 1-4: ").strip().lower()

        if choice in ("1", "create"):
            create_video()
        elif choice in ("2", "plan"):
            plan_content()
        elif choice in ("3", "analyze"):
            analyze_posts()
        elif choice in ("4", "exit"):
            print("\nThanks for using CreatorFlow. Happy creating!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
