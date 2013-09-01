This is the source for my slides to [How To Create Amazing Open Source Modules](http://www.djangocon.us/schedule/presentation/28/).

You can view them on [Github Pages](http://kumar303.github.io/build-open-source/).

# Hacking

To build the slides, create a virtualenv and install some dependencies:

    pip install -r requirements.txt

Then run this script:

    ./build.sh

Open `www/index.html` in your favorite web browser.

Deploy the slides to Github Pages:

    npm install
    volo build && volo ghdeploy
