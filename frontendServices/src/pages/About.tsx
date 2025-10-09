import React from "react";
import  Card  from "@/components/ui/Card";
import { BookOpenCheckIcon, Church, Heart, Plus, Sun } from 'lucide-react';

const About: React.FC = () => {
    const features = [
        {
            title: "Our Mission",
            scripture: "Meditate on the word day and night, so that you may be careful to do everything written in it. - Joshua 1:8",
            description: "To make the Bible accessible and engaging through innovative technology.",
            icon: (
                <BookOpenCheckIcon className="w-6 h-6 text-blue-500" />
            ),
        },
        {
            title: "Our Vision",
            scripture: "All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness. - 2 Timothy 3:16",
            description: "To create a global community of Bible readers and learners.",
            icon: (
                <Sun className="w-6 h-6 text-blue-500" />
            ),
        },
        {
            title: "Our Values",
            scripture: "Finally, brothers and sisters, whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely, whatever is admirable—if anything is excellent or praiseworthy—think about such things. - Philippians 4:8",
            description: "Integrity, innovation, and inclusivity in all we do.",
            icon: (
                <Heart className="w-6 h-6 text-blue-500" />
            ),
        },
        {
            title: "Join Us",
            scripture: "Let us not give up meeting together, as some are in the habit of doing, but let us encourage one another—and all the more as you see the Day approaching. - Hebrews 10:25",
            description: "If youre interested in using this app sign up for our beta program. so we can keep you updated on our progress and have a better count of interested users.",
            icon: (
                <Plus className="w-6 h-6 text-blue-500" />
            ),
        }
    ];

    return (
        <div className="max-w-4xl mx-auto px-6 py-16">
            <div className="text-center mb-12">
                <Church size={64} className="mx-auto text-blue-600 mb-6" />
                <h1 className="text-4xl font-bold text-gray-900 mb-4">About Us</h1>
                <p className="text-lg text-gray-600 leading-relaxed">
                    Learn more about our mission, vision, and help us understand whos interested.
                </p>
            </div>

            <div className="grid md:grid-cols-2 gap-8">
                {features.map((feature, index) => (
                    <Card key={index} hover padding="md">
                        <div className="flex items-center space-x-4 mb-4">
                            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                                {feature.icon}
                            </div>
                            <h3 className="text-lg font-semibold text-gray-900">{feature.title}</h3>
                        </div>
                        <p className="text-gray-600 italic mb-2">"{feature.scripture}"</p>
                        <p className="text-gray-600 leading-relaxed">{feature.description}</p>
                    </Card>
                ))}
            </div>
        </div>
    );
};

export default About;