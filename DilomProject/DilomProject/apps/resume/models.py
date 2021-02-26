from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    resume_PIB = models.CharField(
        'Your name',
        max_length = 64,
    )
    
    resume_email = models.EmailField(
        'Email',
        max_length = 20,
    )
        
    resume_adress = models.CharField(
        'Home adress',
        max_length = 150,
    )
    
    resume_phone = models.CharField(
        'Phone number',
        max_length = 20,
    )
    
    resume_github = models.URLField(
        'Github link',
        max_length = 30,
        blank=True,
    )
    
    resume_position = models.CharField(
        'Position',
        max_length = 30,
    )
    
    resume_experience = models.CharField(
        'Experience',
        max_length = 30,
    )
    
    resume_years = models.CharField(
        'Years',
        max_length = 3,
    )
    
    resume_education = models.CharField(
        'Education',
        max_length = 30,
    )
           
    resume_lng_c_plus = models.CharField(
        'C/C++',
        max_length = 20,
    )
    
    resume_lng_c_sharp = models.CharField(
        'C#',
        max_length = 20,
    )
    
    resume_lng_pascal = models.CharField(
        'Pascal',
        max_length = 20,
    )
    
    resume_lng_java = models.CharField(
        'Java',
        max_length = 20,
    )
    
    resume_lng_html_css = models.CharField(
        'Html/Css',
        max_length = 20,
    )
    
    resume_lng_JS = models.CharField(
        'JavaScript',
        max_length = 20,
    )
    
    resume_lng_Bootstrap = models.CharField(
        'Bootstrap',
        max_length = 20,
    )
    
    resume_lng_php = models.CharField(
        'PHP',
        max_length = 20,
    )
    
    resume_lng_python = models.CharField(
        'Python',
        max_length = 20,
    )
    
    resume_lng_django = models.CharField(
        'Django',
        max_length = 20,
    )
    
    resume_lng_NET = models.CharField(
        '.Net',
        max_length = 20,
    )
    
    resume_lng_nodejs = models.CharField(
        'Node.js',
        max_length = 20,
    )
    
    resume_cms_wordpress = models.CharField(
        'Wordpress',
        max_length = 20,
    )
    
    resume_cms_joomla = models.CharField(
        'Joomla',
        max_length = 20,
    )
    
    resume_cms_drupal = models.CharField(
        'Drupal',
        max_length = 20,
    )
    
    resume_os_windows = models.CharField(
        'Windows',
        max_length = 20,
    )
    
    resume_os_linux = models.CharField(
        'Linux',
        max_length = 20,
    )
    
    resume_os_macos = models.CharField(
        'MacOS',
        max_length = 20,
    )
    
    resume_english = models.CharField(
        'English',
        max_length = 20,
    )
    
    resume_date = models.DateTimeField(
        'Date public resume'
    )
        
    def __str__(self):
        return self.resume_PIB
        
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'
    
        
class Comment(models.Model):
    resume = models.ForeignKey(Resume, on_delete = models.CASCADE)
    author_name = models.CharField(
        'Author name',
        max_length = 50
    )
    
    comment_type = models.CharField(
        'Comment type',
        max_length = 20
    )
    
    comment_text = models.TextField(
        'Comment text'
    )
    
    system_position = models.CharField(
        'System position',
        max_length = 30, 
        blank=True,)
    
    def __str__(self):
        return self.author_name
        
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Images(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
class Position_Area(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    system_position = models.CharField('System position', max_length = 30, blank=True,)
    system_area = models.CharField('System area', max_length = 30, blank=True,)
    
    
    
    