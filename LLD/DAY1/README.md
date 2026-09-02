>UML (Unified Modeling Language) diagrams are the bllueprint of the sft. systems, providing visual represnetation of architecture, interaction and behavior. In another word we can say that UML is the gap between ideas and implementation. 
>
>Now we dive deep into essential UML  diagrams with practical examplex...
>
> ## Why UML diagram Matter
>- **Clarity:** Replace verbose description with intuitive visuals.
>- **Design Validation:** Identify flaws before coding begins.
>- **Documentation:** Serve as living artifacts for futture maintenance.
>- **Communication:** Align teams on system structure and behavior.
>
<p align="center">
  <a href="./img/UML-type.png">
    <img 
      src="./img/UML-type.png" 
      height="700" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>UML Diagram</em>
  </p>
</p>

We'll focus on the Class Diagram (structural) and Sequence Diagram (behavioral) — the most critical for system design interviews.

## Class Diagrams:

Class diagrams depict classes, attributes, methods, and relationships between objects.

**Anatomy of a Class**

<p align="center">
  <a href="./img/anatomy-of-a-class.png">
    <img 
      src="./img/anatomy-of-a-class.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Anatomy of a Class</em>
  </p>
</p>

- **Top Section:** Class Name — Student
- **Middle Section:** Attributes (Fields) — e.g., name, rollNumber, email, age, and cgpa, each with its data type and access modifier:
    - `+ Public`
    - `- Private`
    - `# Protected`
- **Bottom Section:** Methods (Behaviors) — e.g., enrollCourse(), updateEmail(), calculateCGPA(), isEligibleForPlacement(), and getStudentInfo(), including their parameters and return types...

