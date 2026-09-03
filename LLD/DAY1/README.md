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

## Class Associations

Relationships define how classes interact. Types of Associations are:
1) **Inheritance (Is-a Relationship)**
- Arrow: Solid line with a closed triangle
- Example: FullTimeEmployee is a Employee
<p align="center">
  <a href="./img/class-associations.png">
    <img 
      src="./img/class-associations.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Class Associations</em>
  </p>
</p>

2) **Composition (Strong Has-a)**
- Symbol: Filled diamond (◆). Parts cannot exist without the whole.
- Example: A `House` has `Room` and `Door`
<p align="center">
  <a href="./img/composition.png">
    <img 
      src="./img/composition.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Composition</em>
  </p>
</p>

3) **Aggregation (Weak Has-a)**
- Symbol: Hollow diamond (◇). Parts can exist independently.
- Example: A `Department` has a `Employee` and `Project` 
<p align="center">
  <a href="./img/Aggregation.png">
    <img 
      src="./img/Aggregation.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Aggregation</em>
  </p>
</p>

4) **Simple Association**
- Symbol:Open arrow (→). Basic dependency.
- Example: `Teacher` teaches `Student`
<p align="center">
  <a href="./img/Simple-Association.png">
    <img 
      src="./img/Simple-Association.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Simple Association</em>
  </p>
</p>

## Sequence Diagrams: Dynamic Interactions

Sequence diagrams visualize object interactions over time, crucial for behavioral scenarios.
<p align="center">
  <a href="./img/Sequence-dg-entities.png">
    <img 
      src="./img/Sequence-dg-entities.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>Core Components</em>
  </p>
</p>

- **Objects**: Rectangles
- **Lifeline**: Dashed vertical line.
- **Activation Bar**: Thin rectangle (when object is active).

`Messages:`
- **Synchronous:** Solid line + closed arrow ( waits for response).
- **Asynchronous:** Solid line + open arrow (doesn’t wait).
- **Return:** Dashed line (response).
- **Lost:** Message not received.
- **Found:** Message from an unknown source.

### ATM money withdrawal Example:
<p align="center">
  <a href="./img/ATM-Money-Withdrawl.png">
    <img 
      src="./img/ATM-Money-Withdrawl.png" 
      height="500" 
      alt="Architecture diagram"
    />
  </a>
  <p align="center">
    <em>ATM Money Withdrawal</em>
  </p>
</p>