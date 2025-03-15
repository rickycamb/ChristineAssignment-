class Dog:
    def make_sound(self):
        return "Woof"

class Cat:
    def make_sound(self):
        return "Meow"

def process_sound(sound_object):
    # Call the make_sound method on the passed object
    sound = sound_object.make_sound()
    print(f"The sound is: {sound}")

# Example usage:
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: The sound is: Woof
process_sound(cat)  # Output: The sound is: Meow
