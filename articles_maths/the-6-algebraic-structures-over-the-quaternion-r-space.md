# __The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

The six products of *The 6 Products of the Quaternion Real Space* carry six structures on the same four-dimensional real space, and the six structures are named once here and cited by their abbreviations throughout the chapter:

$$
\mathrm{GPA} , \quad \mathrm{SPA} , \quad \mathrm{APA} , \quad \mathrm{GQA} , \quad \mathrm{SQA} , \quad \mathrm{AQA} .
$$

The **general plain algebra** $\mathrm{GPA}$ is the space with the general plain bilinear product $\tilde p\tilde q$; the **symmetric plain algebra** $\mathrm{SPA}$ with the Jordan product $\tilde p\bullet\tilde q$; the **antisymmetric plain algebra** $\mathrm{APA}$ with the cross product $\tilde p\wedge\tilde q=\vec p\times\vec q$; the **general quaternionic algebra** $\mathrm{GQA}$ with the general quaternionic product $\tilde p^{\natural}\tilde q$; the **symmetric quaternionic algebra** $\mathrm{SQA}$ with the product $N(\tilde p,\tilde q)e_0$; and the **antisymmetric quaternionic algebra** $\mathrm{AQA}$ with the quaternionic cross product $\tilde p\wedge^{\natural}\tilde q$. The same space carries the six, and the six are told apart by the laws their products satisfy; this article gives the names, the structure of each, the law table and the two laws that single out two of the six.

The article assumes the six products and their coordinate rules from *The 6 Products of the Quaternion Real Space*, the article preceding this one, and the definitions of the vocabulary it uses from *Definitions for the Study of the 6 Algebraic Structures*, below this article in this category.

**Conventions.** Throughout, $\mathbb{H}$ is the real quaternion algebra with units $e_0,e_1,e_2,e_3$, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, and the six products are written $\tilde p\tilde q$, $\tilde p\bullet\tilde q$, $\tilde p\wedge\tilde q=\vec p\times\vec q$, $\tilde p^{\natural}\tilde q$, $N(\tilde p,\tilde q)e_0$ and $\tilde p\wedge^{\natural}\tilde q$. The **support** of a structure is the underlying real vector space, which is $\mathbb{H}$ for all six.

## The Six Names and Their Structures

| abbreviation | name | product | structure |
|---|---|---|---|
| $\mathrm{GPA}$ | general plain algebra | $\tilde p\tilde q$ | associative unital algebra, a division algebra |
| $\mathrm{SPA}$ | symmetric plain algebra | $\tilde p\bullet\tilde q$ | commutative Jordan algebra |
| $\mathrm{APA}$ | antisymmetric plain algebra | $\tilde p\wedge\tilde q=\vec p\times\vec q$ | Lie algebra, alternating |
| $\mathrm{GQA}$ | general quaternionic algebra | $\tilde p^{\natural}\tilde q$ | non-associative algebra with a left unit |
| $\mathrm{SQA}$ | symmetric quaternionic algebra | $N(\tilde p,\tilde q)e_0$ | commutative, scalar-valued rule |
| $\mathrm{AQA}$ | antisymmetric quaternionic algebra | $\tilde p\wedge^{\natural}\tilde q$ | alternating, non-Lie rule |

The support of each is the whole space $\mathbb{H}$, of real dimension four; no structure has a smaller support, and each product is determined by its values on the pairs of the four units. The adjectives **general**, **symmetric** and **antisymmetric** name the half from which the product comes — the product itself, its symmetric part, or its antisymmetric part — and the adjectives **plain** and **quaternionic** name the family of the general product from which it descends.

## The Law Table

The table lists, for each of the six, the symmetry or alternation of the product, the laws it satisfies, the laws it fails and its unit or units. The witnesses for the failures are those of the two-product table of *Comparison Between the Two General Products*, the article preceding this one, completed by the halves.

| structure | symmetry | laws satisfied | laws failed | unit |
|---|---|---|---|---|
| $\mathrm{GPA}$ | neither | associative; flexible; power-associative; Jordan | commutative | $e_0$ two-sided |
| $\mathrm{SPA}$ | symmetric | commutative; Jordan; flexible; power-associative | associative; alternative | $e_0$ two-sided |
| $\mathrm{APA}$ | antisymmetric, alternating | Jacobi; flexible; power-associative | associative; commutative; alternative; unit | none |
| $\mathrm{GQA}$ | neither | left unit | associative; commutative; flexible; power-associative; alternative; right unit | $e_0$ left only |
| $\mathrm{SQA}$ | symmetric | commutative; flexible; power-associative | associative; Jordan; alternative; unit | none |
| $\mathrm{AQA}$ | antisymmetric, alternating | flexible; power-associative | Jacobi; associative; commutative; alternative; unit | none |

Three rows of the table are read at once. **A symmetric product is flexible and power-associative**, because the two identities are read on the same argument twice and the symmetry interchanges the two readings; this gives the second and third rows of the table for $\mathrm{SPA}$ and $\mathrm{SQA}$. **An antisymmetric product is alternating, flexible and power-associative**, because $f(\tilde p,\tilde p)=-f(\tilde p,\tilde p)=0$ makes every square zero and the flexibility reads the antisymmetry once on each side; this gives the two rows for $\mathrm{APA}$ and $\mathrm{AQA}$, and it makes the cubes of the two zero. And **the unit survives only where the product agrees with the general one on the unit**: the symmetric half of the plain product keeps the two-sided unit $e_0$, while the symmetric half of the quaternionic product has none, being scalar valued, $e_0$ acting there as $N(e_0,\tilde q)e_0=q_0e_0=\mathrm{Sc}(\tilde q)e_0$.

## The Two Laws of the Table

**Theorem (the two laws).** Among the six structures, the general plain algebra is the only one whose product is associative, and the antisymmetric plain algebra is the only one whose product satisfies the Jacobi identity.

*Proof.* The general plain product is the multiplication of $\mathbb{H}$, associative. Associativity fails for the other five, and the failures are read on the basis triples: it fails for the general quaternionic product on $(\tilde p,\tilde q,\tilde r)=(e_1,e_1,e_1)$, as in *Comparison Between the Two General Products*; for the Jordan product and for the cross product it fails on $(e_1,e_1,e_2)$, where the associators are $-e_2$ and $+e_2$ respectively, since $e_1\wedge(e_1\wedge e_2)=e_1\wedge e_3=-e_2$ while $(e_1\wedge e_1)\wedge e_2=0$ and the same value with the sign reversed for the Jordan product; and for the symmetric quaternionic product and the quaternionic cross product it fails on the triples $(e_0,e_1,e_1)$ and $(e_0,e_0,e_1)$ respectively, where the associators are $-e_0$ and $-e_1$, the symmetric quaternionic product sending the products $e_0\bullet e_1$ and $e_0\bullet e_0$ to scalars and so breaking the parenthesis. The Jacobi identity, $\tilde p\wedge(\tilde q\wedge\tilde r)+\tilde q\wedge(\tilde r\wedge\tilde p)+\tilde r\wedge(\tilde p\wedge\tilde q)=0$, holds for the cross product because the cross product of vectors is the Lie bracket of the Lie algebra $\mathbb{R}^3=\mathfrak{so}(3)$; it fails for the quaternionic cross product, on the triple $(e_0,e_1,e_2)$ giving $e_3$; for the general plain product the cyclic sum does not vanish either, being $-3e_0$ on the triple $(e_1,e_2,e_3)$, where the product of the three factors is $-e_0$; and for the general quaternionic product and the two symmetric products the cyclic sums likewise do not vanish. Both statements are decided on the basis triples alone.

The two laws are the two rows of the menu that isolate two of the six, and they are the reason the chapter speaks of a Jordan layer and a Lie layer. The plain product is the only one of the six that is a multiplication in the strict sense of an associative algebra with unit; the cross product is the only one that is a Lie bracket; the other four carry weaker laws, and the two products of the quaternionic family carry no law beyond the left unit and the flexibility and power-associativity of their halves.

## The Reading of the Other Five Products

The blocks that follow read each of the six structures in turn. The general plain algebra is *Introduction to the General Plain Algebra of Quaternions*; the symmetric plain algebra is *Introduction to the Symmetric Plain Algebra of Quaternions*; the antisymmetric plain algebra is *Introduction to the Antisymmetric Plain Algebra of Quaternions*; the general quaternionic algebra is *Introduction to the General Quaternionic Algebra of Quaternions*; the symmetric quaternionic algebra is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; and the antisymmetric quaternionic algebra is *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, all in the six blocks that follow this group. Each of the six articles reads the product of the structure as a multiplication, with its own units, its own zero divisors and its own classes of element, using the vocabulary of *Definitions for the Study of the 6 Algebraic Structures*, below this article in this category.

**Remark (the same space six times).** The six structures are not six algebras in the sense of six different vector spaces: they are one space with six products, and the vocabulary of the chapter is indexed by the product and not by the space. An element may be a unit for $\mathrm{GPA}$ and not for $\mathrm{SPA}$, a zero divisor for $\mathrm{SPA}$ and not for $\mathrm{GPA}$, and every element is a square-zero element for the two antisymmetric structures and for them alone.

## Summary

The quaternion space carries six algebraic structures on the same four-dimensional real support, named once here: the general plain algebra $\mathrm{GPA}$ with $\tilde p\tilde q$, the symmetric plain algebra $\mathrm{SPA}$ with the Jordan product, the antisymmetric plain algebra $\mathrm{APA}$ with the cross product, the general quaternionic algebra $\mathrm{GQA}$ with $\tilde p^{\natural}\tilde q$, the symmetric quaternionic algebra $\mathrm{SQA}$ with $N(\tilde p,\tilde q)e_0$ and the antisymmetric quaternionic algebra $\mathrm{AQA}$ with the quaternionic cross product. The structures are an associative unital division algebra, a commutative Jordan algebra, a Lie algebra, a non-associative left-unital algebra, a commutative scalar-valued rule and an alternating non-Lie rule.

The law table separates them: the symmetric products are commutative, flexible and power-associative; the antisymmetric products are alternating, flexible and power-associative, with cubes zero; the general plain product is associative, flexible and Jordan but not commutative; the general quaternionic product has a left unit alone and fails associativity, commutativity, flexibility and power-associativity; and the symmetric quaternionic product is commutative and power-associative but neither associative nor Jordan. The two laws of the table are that the general plain algebra is the only associative one and the antisymmetric plain algebra the only one satisfying Jacobi.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{GPA}$ | general plain algebra, the associative division algebra of $\tilde p\tilde q$ |
| $\mathrm{SPA}$ | symmetric plain algebra, the Jordan algebra of $\tilde p\bullet\tilde q$ |
| $\mathrm{APA}$ | antisymmetric plain algebra, the Lie algebra of $\tilde p\wedge\tilde q=\vec p\times\vec q$ |
| $\mathrm{GQA}$ | general quaternionic algebra, the left-unital rule $\tilde p^{\natural}\tilde q$ |
| $\mathrm{SQA}$ | symmetric quaternionic algebra, the scalar rule $N(\tilde p,\tilde q)e_0$ |
| $\mathrm{AQA}$ | antisymmetric quaternionic algebra, the rule $\tilde p\wedge^{\natural}\tilde q$ |
| support | the space $\mathbb{H}$, of real dimension four, for all six |
| the two laws | only $\mathrm{GPA}$ associative; only $\mathrm{APA}$ satisfying Jacobi |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan product, its identities and the algebra it defines.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Jacobi identity, the alternating bracket and the Lie algebra of the cross product.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for associativity, the unit and the symmetrisation of a bilinear product.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the six products of the quaternion space and their companion algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the place of the cross product and the quaternion product among the Clifford products.
