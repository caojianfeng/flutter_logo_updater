
# flutter_logo_updater
Tool to update all app icons in flutter project

## Installing:
```bash
pip install flutter_logo_updater
```

## Using:
flutter_logo_updater logo_file_path project_file_path

Exmple:
```txt
flutter_logo_updater msks/images/logo_lxb.png msks/
```

## How does it work:

### 1. Find a config

Find a config from your_flutter_project/flutter_logo_updater.json

If no config found a default cfg while be use.

```json
{
    "ios": {
        "appiconset": "ios/Runner/Assets.xcassets/AppIcon.appiconset"
    },
    "android": {
        "manifest": "android/app/src/main/AndroidManifest.xml"
    }
}
```

### 2. Find icon infos

To kown which png shoud be replaced.

#### 2.1 On iOS

##### 2.1.1 Find icons by the AppIcon.appiconset/Contents.json 

##### 2.1.2 Get the image_filename and size info from the json.

```json
{
  "images" : [
        {
            "size" : "20x20",
            "idiom" : "iphone",
            "filename" : "Icon-App-20x20@2x.png",
            "scale" : "2x"
        },
        {
            "..."
        }
    ]
}
```

#### 2.2 On Android

#### 2.2.1 Find the android:icon prop of manifest/application from AndroidManifest.xml

```xml
<manifest>
    <application
        android:icon="@mipmap/ic_launcher">
        <!-- ... -->
    </application>
</manifest>
```

##### 2.2.2 Parse base_dir from android:icon

So flutter_logo_updater kown which dir to search, mipmap or drawble.

##### 2.2.3 Search png files and read their size.

### 3. Resize you logo(1024*1024) to sizes of the icons and replace them. 

