---
title: "How to Downgrade Home Assistant Add-ons: A Step-by-Step Guide"
description: "Learn how to effectively downgrade your Home Assistant add-ons to prevent issues and ensure optimal performance with this detailed guide."
pubDate: 2026-07-02
category: home-assistant
tags:
  - Home Assistant
  - Add-ons
  - Downgrade
  - Smart Home
image: "/images/how-to-downgrade-home-assistant-add-ons-a-step-by-step-guide.jpg"
imageAlt: "turned-on charcoal Google Home Mini and smartphone"
imageKeyword: "home assistant interface"
draft: false
---

Downgrading an add-on in Home Assistant isn’t just a techie hack; it’s often a necessary step to restore stability or functionality after an upgrade goes haywire. Whether you've encountered bugs in the latest version or simply prefer features from an earlier release, being able to downgrade can save you from unnecessary headaches. Here’s how to do it efficiently, along with practical tips for managing your add-ons.

## The Bottom Line: Manual Downgrade via Supervisor

The easiest method to downgrade a Home Assistant add-on is through the Supervisor interface. If you’ve just updated an add-on and are facing issues, follow these steps to revert to a previous version. This method is straightforward, but requires you to have specific version numbers handy.

## Step-by-Step Guide to Downgrading Home Assistant Add-ons

### Prerequisites

Before you start, ensure you have:

1. **Home Assistant Installed**: Make sure your Home Assistant is up and running.
2. **Access to Supervisor**: You need to have the Supervisor add-on installed (which comes in the Home Assistant OS).
3. **Version History**: Know the version number you want to downgrade to.

### Steps to Downgrade

1. **Access Home Assistant**:
   - Open your Home Assistant dashboard by navigating to `http://[YOUR_HOME_ASSISTANT_IP]:8123/`.

2. **Navigate to Supervisor**:
   - Click on the “Supervisor” icon on the left sidebar. You need to be in the main dashboard.

3. **Go to Add-ons**:
   - Click on the “Add-on Store” tab within the Supervisor section. This will list all installed add-ons.

4. **Select the Add-on**:
   - Find the add-on you want to downgrade and click on it. This reveals information about the add-on.

5. **View Versions**:
   - Scroll down to the bottom to find the “Version” section. Here, you will see the current version installed, and below it, the “Add-on version history.”

6. **Choose Previous Version**:
   - Click on the version you wish to downgrade to. If it’s not displayed, you may have to check the add-on’s documentation or repository for available versions.

7. **Install the Previous Version**:
   - Click on "Install" or "Update". This will handle the downgrade automatically.

8. **Restart Home Assistant**:
   - After installation, restart Home Assistant for changes to take effect. This can usually be done in the Supervisor panel.

### Example: Downgrading the Node-RED Add-on

If you're using the Node-RED add-on and encounter performance issues after an update, you can follow the steps outlined above. Let’s say you just upgraded to version 12.0 but found that a previously stable version was 11.5. After performing the steps:

1. You locate Node-RED in the add-ons.
2. You select version 11.5 from the version history.
3. You confirm the installation, and after Home Assistant restarts, you should find improved performance.

## Troubleshooting Downgrade Issues

Sometimes, downgrading may not solve the problem or you might encounter new issues. Here are some fixes:

- **Rollback Configuration**: Restore any configuration files related to the add-on if they were changed during the update.
- **Log Files**: Check Home Assistant log files for error messages. This can shed light on unresolved issues.
- **Community Forums**: If you're stuck, consult the Home Assistant community for advice on similar issues.

## Who Should Skip This Guide?

If you’re someone who doesn’t frequently use add-ons or is content with the latest features and improvements, downgrading likely won't appeal to you. Also, if you’re managing your Home Assistant environment with a more hands-off approach or relying on core functionalities without add-ons, follow the latest updates for an enhanced experience. 

## Who This Guide Is For

This guide is perfect for:

- **Developers or Tech Enthusiasts**: If you are testing different add-on versions for stability or functionality.
- **Everyday Users Struggling with Bugs**: If you’ve recently updated an add-on and started facing bugs or performance issues, this guide will help you return to a stable version.

## Conclusion

Downgrading Home Assistant add-ons is an essential skill to preserve your smart home environment's functionality. The steps provided are simple and effective, allowing you to revert to previous versions when updates cause more harm than good. Always remember to back up your configurations and stay updated on version histories for the best experience.

By following this guide, you can quickly regain control over your Home Assistant setup. If you find yourself downgrading often, consider weighing the pros and cons of each add-on update more critically or checking the Home Assistant community for best practices.

Just remember — avoid panic. The ability to downgrade is there for a reason, and with a few clicks, your smart home can return to its well-functioning state.