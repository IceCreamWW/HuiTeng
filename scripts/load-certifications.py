import os
os.chdir('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Huiteng.settings")

certifications = [
    ('CE认证', '/img/certifications/CE认证.jpg',
     ['/img/certifications/CE认证.jpg'], True),

    ('船级社认证-气体保护电弧焊焊丝', '/img/certifications/船级社认证-气体保护电弧焊焊丝.jpg',
     ['/img/certifications/船级社认证-气体保护电弧焊焊丝.jpg',
      '/img/certifications/船级社认证-气体保护电弧焊焊丝-1.jpg',
      '/img/certifications/船级社认证-气体保护电弧焊焊丝-2.jpg'], True),

    ('船级社认证-耐候钢气体保护焊焊丝', '/img/certifications/船级社认证-耐候钢气体保护焊焊丝.jpg',
     ['/img/certifications/船级社认证-耐候钢气体保护焊焊丝.jpg',
      '/img/certifications/船级社认证-耐候钢气体保护焊焊丝-1.jpg',
      '/img/certifications/船级社认证-耐候钢气体保护焊焊丝-2.jpg'], True),

    ('质量体系认证', '/img/certifications/质量体系认证.jpg',
     ['/img/certifications/质量体系认证.jpg'], True),
]
if __name__ == '__main__':
    import django
    django.setup()
    from index.models import Certifications
    for c in certifications:
        certification = Certifications(name=c[0], cover_img_path=c[1], all_img_paths=c[2], visible=c[3])
        certification.save()

