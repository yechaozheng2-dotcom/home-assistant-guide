---
title: "How to Use Home Assistant Kiosk Mode for Your Smart Home"
description: "Step-by-step guide to setting up Kiosk Mode in Home Assistant for dedicated devices."
pubDate: 2026-07-21
category: home-assistant
tags:
  - Home Assistant
  - Kiosk Mode
  - Smart Home Automation
  - Configurations
image: "/images/how-to-use-home-assistant-kiosk-mode-for-your-smart-home.jpg"
imageAlt: "a tablet sitting on top of a wooden table next to a cup of coffee"
imageKeyword: "tablets displaying home assistant"
draft: false
---

Are you looking to turn a tablet or display into a dedicated Home Assistant interface? Kiosk Mode is your solution. It's perfect for families, shared spaces, or just simplifying access to your home automation controls without distractions. This guide will help you set up Kiosk Mode, ensuring your devices are tailored for easy interaction with Home Assistant.

### Prerequisites

- **Skill Level**: Beginner
- **Time Estimate**: Approximately 30 minutes
- **Required Tools**:
  - A device (tablet, Raspberry Pi, or smart display) running a modern browser.
  - Access to your Home Assistant instance (e.g., `http://your-home-assistant-address:8123`).
  - Basic understanding of YAML configurations.

### Step-by-Step Instructions

#### Step 1: Install the Kiosk Mode Add-On
**Action**: Navigate to the Home Assistant Supervisor panel, then select "Add-on Store." Find the "Kiosk Mode" add-on and install it.

**Why it matters**: Kiosk Mode allows your device to run a full-screen version of Home Assistant, preventing users from accessing other apps or settings.

**Common Mistake**: Forgetting to enable the add-on after installation. Make sure to click on "Start" in the add-on settings.

#### Step 2: Configure the Kiosk Mode Add-On
**Action**: Click on the "Kiosk Mode" add-on to access its configuration options. Adjust the following fields in the **Configuration** tab:
```yaml
username: "your_username" # Replace with your Home Assistant username
password: "your_password" # Replace with your Home Assistant password
url: "/lovelace/default_view" # The URL of the dashboard you want to display
```

**Why it matters**: The username and password provide secure access, while the URL specifies what the Kiosk Mode should show.

**Common Mistake**: Leaving the credentials as defaults. Always change the password to a unique one for security.

#### Step 3: Setup the Kiosk View
**Action**: If you want a specific dashboard or view, create one under the Lovelace UI. For instance, go to the Dashboard settings, create a new view and customize it to your needs.

**Why it matters**: A tailored dashboard offers quick access to the most frequented devices and controls, streamlining user interactions.

**Common Mistake**: Failing to set up the correct view name in the Kiosk configuration. Ensure you use the right path.

#### Step 4: Launch Kiosk Mode
**Action**: Open the device browser and type in the URL of your Home Assistant with the Kiosk settings. Make sure to exclude the trailing `/`.

**Why it matters**: This allows the Kiosk Mode to lock onto the specified URL and function as intended without showing browser elements.

**Common Mistake**: Using the wrong Home Assistant URL or IP address, which leads to being unable to access the dashboard.

#### Step 5: Final Touches
**Action**: Enable the Kiosk Mode settings such as hiding the address bar and disabling navigation to ensure the interface runs smoothly.

**Why it matters**: This keeps the Kiosk experience clean and user-friendly, ensuring that the user remains focused on the smart home control features.

**Common Mistake**: Not configuring kiosk settings properly can result in a traditional browser experience rather than a dedicated interface.

### Troubleshooting Common Issues

**If you see a login screen instead of the dashboard**:  
- **Do**: Verify that you have entered the correct username and password in the Kiosk configuration.

**If the dashboard is not responsive**:  
- **Do**: Check if the URL is correct and ensure the Lovelace dashboard is properly configured.

**If Kiosk Mode doesn’t start**:  
- **Do**: Ensure the Kiosk Mode add-on is running by checking the Supervisor panel.

**If the screen orientation is incorrect**:  
- **Do**: Depending on the device, adjust the display settings to portrait or landscape mode based on your preference.

**If interactions are not working as expected**:  
- **Do**: Make sure that your Home Assistant instance is not behind a firewall or that any network restrictions are lifted to ensure communication.

### Variations and Next Steps

Once you have Kiosk Mode up and running, consider enhancing your setup further:
- **Widgets and Custom Cards**: Add interactive components to your dashboard, enhancing usability for different family members or guests.
- **Voice Command Integration**: Use Google Assistant or Amazon Alexa to control your Home Assistant setups hands-free.
- **Touch Feedback**: For Raspberry Pi setups, consider using a touchscreen interface for a more interactive kiosk experience.

Take the time to explore and customize your Kiosk Mode setup. The more tailored it becomes to your needs, the better your smart home interaction will be. Whether you plan to use it in a busy family environment or for monitoring your smart appliances, Kiosk Mode makes home automation accessible and engaging for everyone.