# __Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

The six structures of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* are read through a vocabulary of elements and of identities which the six blocks that follow use without restating it. This article fixes that vocabulary once: the **element vocabulary** — the square, the powers, the unit and the units, the inverse, the radical, the zero divisor, the idempotent, the nilpotent and the square root of a central value — is stated for an arbitrary real-bilinear product and then read on the six; the **identity vocabulary** — alternating, flexible, Jordan, Jacobi, power-associative and the degree-three identities — is stated with its mutual implications; and the **criterion for an empty class** is given, the rule by which a class defined by an equation is recognized as empty from the laws of the product alone.

Nothing here is a theorem about the quaternion space; the article is the common grammar of the six blocks, and every statement in it is a definition or an implication among definitions. The six products and the six structures are those of *The 6 Products of the Quaternion Real Space* and *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the two articles preceding this one.

**Conventions.** Throughout, $f$ is a real-bilinear binary rule on the space $\mathbb{H}$, written multiplicatively $f(x,y)=xy$ in the statements about a general product, and $x,y,z$ name elements. When the product of a statement is one of the six, it is named by its abbreviation of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The element $0$ is the zero vector and $e$ names a unit.

## The Element Vocabulary

Let $f$ be a real-bilinear rule on $\mathbb{H}$.

**Square and powers.** The **square** of $x$ is $x^2=f(x,x)$ and the **powers** are $x^1=x$, $x^{k+1}=f(x,x^k)$. The square is the only power used in the six blocks; the powers $x^k$ for $k\geq3$ are well defined for every rule, being left-nested products of $k$ copies of $x$.

**Unit.** An element $e$ is a **left unit** when $f(e,x)=x$ for every $x$, a **right unit** when $f(x,e)=x$ for every $x$, and a **two-sided unit** or **unit** when both. A rule has at most one two-sided unit.

**Inverse and units.** When the rule has a two-sided unit $e$, the **inverse** of $x$ is the element $y$ with $f(x,y)=e=f(y,x)$, and $x$ is **invertible** or a **unit** when it has an inverse. Without a two-sided unit the word inverse is not used; the six blocks say instead that an element is **regular** for a one-sided unit.

**Radical.** The **radical** of the rule is

$$
\operatorname{rad}(f)=\{x:f(x,y)=0=f(y,x)\ \text{for every}\ y\} ,
$$

the two-sided annihilator of the whole space; it is a subspace, and the rule is **nondegenerate** when the radical is $\{0\}$.

**Zero divisor.** A nonzero element $x$ is a **left zero divisor** when $f(x,y)=0$ for some nonzero $y$, a **right zero divisor** when $f(y,x)=0$ for some nonzero $y$, and a **zero divisor** when either. A rule with no zero divisor and a two-sided unit is a **division rule**, and an algebra whose rule is a division rule is a **division algebra**.

**Idempotent.** An **idempotent** is an element with $x^2=x$; the idempotents form a set containing $0$ and every unit.

**Nilpotent.** A **nilpotent** is a nonzero element with $x^k=0$ for some $k$; the case $k=2$, $x^2=0$, is a **square-zero** element and the case $k=3$, $f(x,f(x,x))=0$, a **cube-zero** element. Nilpotents are the nonzero elements of the class the six blocks call the **nilpotent class**.

**Square root of a central value.** The **centre** of the rule is $\{z:f(z,x)=f(x,z)\ \text{for every}\ x\}$; a **square root of a central value** $c$ is an element $x$ with $x^2=c$ and $c$ in the centre. A central value may have no square root, one, or a class of them, and the class is the set $\{x:x^2=c\}$.

## The Identity Vocabulary

**Alternating.** The rule is **alternating** when $f(x,x)=0$ for every $x$.

**Flexible.** The rule is **flexible** when $f(f(x,y),x)=f(x,f(y,x))$ for all $x,y$.

**Jordan.** The rule satisfies the **Jordan identity** when $f(f(f(x,x),y),x)=f(f(x,x),f(y,x))$ for all $x,y$, that is $(x^2y)x=x^2(yx)$.

**Jacobi.** The rule satisfies the **Jacobi identity** when

$$
f(x,f(y,z))+f(y,f(z,x))+f(z,f(x,y))=0
$$

for all $x,y,z$.

**Power-associative.** The rule is **power-associative** when $f(f(x,x),x)=f(x,f(x,x))$ for every $x$, so that the two nestings of the cube agree and all powers are unambiguous.

**Degree-three identities.** The identities of **degree three** are the identities in which one factor of a product is itself a product: **associativity**, $f(f(x,y),z)=f(x,f(y,z))$; the **left alternative** identity, $f(f(x,x),y)=f(x,f(x,y))$; the **right alternative** identity, $f(f(y,x),x)=f(y,f(x,x))$; and **flexibility**, which is obtained from associativity by replacing $z$ with $x$ in both sides. A rule is **alternative** when both alternative identities hold, and **associative** when so does associativity.

**Implications.** The following implications among the identities are the ones the six blocks use; each is immediate from the definitions and the bilinearity.
- **Associative $\Rightarrow$ flexible, power-associative, Jordan.** An associative rule inserts and removes parentheses freely, so the two nestings of the cube agree, the flexibility is two writings of the same triple product, and the Jordan identity is the reading of $x^2yx$ on both sides.
- **Alternating and bilinear $\Rightarrow$ flexible, power-associative, cube-zero.** A bilinear alternating rule is antisymmetric, $f(y,x)=-f(x,y)$, since $f(x+y,x+y)=0$; flexibility is then $f(f(x,y),x)=-f(x,f(x,y))=f(x,f(y,x))$, the power identity is read on the square $f(x,x)=0$, and the cube $f(x,f(x,x))=f(x,0)=0$.
- **Symmetric and bilinear $\Rightarrow$ flexible, power-associative.** A symmetric rule interchanges the two slots everywhere, and the flexibility and the power identity each compare two readings of the same arguments, so the interchange makes them equal.
- **Alternating and Jacobi $\Rightarrow$ Lie.** An alternating bilinear rule satisfying the Jacobi identity is a Lie bracket; that is the definition of the Lie structure.

## The Reading on the Six

The table records, for each identity, the structures of the six that satisfy it, on the basis pairs and triples of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

| identity | $\mathrm{GPA}$ | $\mathrm{GQA}$ | $\mathrm{SPA}$ | $\mathrm{SQA}$ | $\mathrm{APA}$ | $\mathrm{AQA}$ |
|---|---|---|---|---|---|---|
| alternating | no | no | no | no | **yes** | **yes** |
| flexible | yes | no | yes | yes | yes | yes |
| power-associative | yes | no | yes | yes | yes | yes |
| Jordan identity | yes | yes | yes | no | yes | yes |
| associative | **yes** | no | no | no | no | no |
| alternative | yes | no | no | no | no | no |
| Jacobi identity | no | no | no | no | **yes** | no |

The reading is the law table of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* reordered by identity rather than by structure, and it obeys the implications above: the two antisymmetric structures are the only alternating ones, they are flexible and power-associative and cube-zero by the second implication; the two symmetric structures are flexible and power-associative by the third; the general plain structure is the only associative one and hence flexible, power-associative and Jordan; and the general quaternionic structure is the only one whose half-products carry no law that the product itself inherits, its first factor being conjugated.

The Jordan identity holds for five of the six, the antisymmetric structures included, and it fails only for the symmetric quaternionic structure: the Jordan identity is weak, and the structure called the Jordan layer is $\mathrm{SPA}$ because its product is symmetric and the identity is the strongest law it has, not because it is the only one satisfying the identity.

## The Criterion for an Empty Class

A class defined by an equation is recognized as empty from the laws of the product alone, and the criterion is one line.

**Criterion.** Let a class be defined by an equation $P(x)=0$ for a polynomial $P$ built from the product. The class is empty when the equation contradicts a law of the product, that is when every element satisfying the law and the equation would violate an identity the product satisfies; otherwise the class is tested on the basis.

The applications the six blocks use are these. The class of **nonzero idempotents** is empty for the two antisymmetric structures, since $x^2=x$ reads $0=x$ there; and it is $\{e_0\}$ for the general plain structure, a nonzero idempotent $x$ being a unit and $x^2=x$ giving $x=e_0$. The class of **nonzero nilpotents** is empty for the general plain and the general quaternionic structures, since $x^2=0$ with $x\neq0$ makes $x$ a zero divisor, and there is none; it is the whole space apart from the origin for the two antisymmetric structures, every nonzero element being square-zero; and it is read on the basis for the two symmetric structures. The class of **units** is empty for the four structures without a two-sided unit, the general quaternionic structure having only a left unit, the antisymmetric ones none, and the symmetric quaternionic one none; and the class of **square roots of the central value $-e_0$** is empty for the four structures whose square is a real-valued expression of one sign, $\mathrm{GQA}$ and $\mathrm{SQA}$ having $x^2=N(x)e_0$ with $N(x)\geq0$ and the two antisymmetric structures having $x^2=0$, while it is nonempty for $\mathrm{GPA}$ and $\mathrm{SPA}$, the unit vector $e_1$ having the square $-e_0$ in both. The algebraic norm functions behind these classes are the two algebraic norms of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, below this article in this category, whose level sets are read there.

## Summary

The element vocabulary of the six structures is the square and the powers, the unit and the units, the inverse, the radical, the zero divisor, the idempotent, the nilpotent and the square root of a central value, each defined for a general real-bilinear product and read on the six. The identity vocabulary is alternation, flexibility, the Jordan identity, the Jacobi identity, power-associativity and the degree-three identities, with the implications: associative implies flexible, power-associative and Jordan; alternating with bilinearity implies antisymmetry, flexibility, power-associativity and cube-zero; symmetric with bilinearity implies flexibility and power-associativity; and alternating with Jacobi is the Lie structure.

The reading on the six gives the antisymmetric structures as the alternating ones, both flexible and power-associative; the symmetric ones as flexible and power-associative; $\mathrm{GPA}$ as the only associative one; the Jordan identity as holding for five of the six and failing for $\mathrm{SQA}$; and the Jacobi identity as holding for $\mathrm{APA}$ alone. A class is empty exactly when its defining equation contradicts a law of the product, and the criterion is applied to the classes of idempotents, nilpotents, units and square roots of a central value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x^2=f(x,x)$, $x^{k+1}=f(x,x^k)$ | square and powers |
| left, right, two-sided unit $e$ | $f(e,x)=x$, $f(x,e)=x$, both |
| inverse of $x$ | $y$ with $f(x,y)=e=f(y,x)$ |
| $\operatorname{rad}(f)=\{x:f(x,y)=0=f(y,x)\ \forall y\}$ | the radical |
| zero divisor | nonzero $x$ with $f(x,y)=0$ or $f(y,x)=0$, $y\neq0$ |
| idempotent | $x^2=x$ |
| nilpotent, square-zero, cube-zero | $x^k=0$; $x^2=0$; $f(x,f(x,x))=0$ |
| square root of a central value | $x$ with $x^2=c$, $c$ central |
| alternating, flexible | $f(x,x)=0$; $f(f(x,y),x)=f(x,f(y,x))$ |
| Jordan, Jacobi | $(x^2y)x=x^2(yx)$; $f(x,f(y,z))+f(y,f(z,x))+f(z,f(x,y))=0$ |
| power-associative, degree three | $f(f(x,x),x)=f(x,f(x,x))$; identities with a nested factor |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, nilpotents, the radical and the units of an algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan identity, power-associativity and the flexible law.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the alternating bilinear rule, the Jacobi identity and the Lie structure.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the centre, the unit and the inverses in a non-commutative ring.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, Universitext, 2004), for the flexibility and power-associativity of a symmetric product.
