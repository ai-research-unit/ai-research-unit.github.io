# __The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

The companion products of *The 6 Products of the Quaternioid Real Space* carry three structures on the same four-dimensional real space, and the three are named once here and cited by their abbreviations throughout the category:

$$
\mathrm{SPA} , \qquad \mathrm{APA} , \qquad \mathrm{GQA} .
$$

The **symmetric plain algebra** $\mathrm{SPA}$ is the space with the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$; the **antisymmetric plain algebra** $\mathrm{APA}$ with the cross product $\tilde p\wedge\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$; and the **general quaternionic algebra** $\mathrm{GQA}$ with the general quaternionic product $\tilde p^{\natural}\tilde q$. The algebra product $\tilde p\tilde q$ makes the space a fourth structure, the quaternionic division algebra, and that one belongs to the *Quaternions* category, cited from here and never restated. The same space carries the three companion structures, and the three are told apart by the laws their products satisfy; this article gives the names, the structure of each, the law table and the two laws that single out two of the three.

The article assumes the products and their coordinate rules from *The 6 Products of the Quaternioid Real Space*, the article preceding this one, and the definitions of the vocabulary it uses from *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

**Conventions.** Throughout, $\mathbb{H}$ is the real quaternion algebra with units $e_0,e_1,e_2,e_3$, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, and the companion products are written $\tilde p\bullet\tilde q$, $\tilde p\wedge\tilde q=\vec p\times\vec q$ and $\tilde p^{\natural}\tilde q$. The **support** of a structure is the underlying real vector space, which is $\mathbb{H}$ for all three.

## The Three Names and Their Structures

| abbreviation | name | product | structure |
|---|---|---|---|
| $\mathrm{SPA}$ | symmetric plain algebra | $\tilde p\bullet\tilde q$ | commutative Jordan algebra with the two-sided unit $e_0$ |
| $\mathrm{APA}$ | antisymmetric plain algebra | $\tilde p\wedge\tilde q=\vec p\times\vec q$ | alternating Lie algebra, without unit |
| $\mathrm{GQA}$ | general quaternionic algebra | $\tilde p^{\natural}\tilde q$ | non-associative algebra with a left unit |

The support of each is the whole space $\mathbb{H}$, of real dimension four; no structure has a smaller support, and each product is determined by its values on the pairs of the four units. The adjectives **symmetric** and **antisymmetric** name the half of the algebra product from which the product comes — its symmetric part or its antisymmetric part; the adjective **quaternionic** names the product with the conjugation read in the first slot.

## The Law Table

The table lists, for each of the three, the symmetry or alternation of the product, the laws it satisfies, the laws it fails and its unit or units. The witnesses for the failures are those of the two-product table of *Comparison Between the Two General Products*, the article preceding this one, completed by the halves.

| structure | symmetry | laws satisfied | laws failed | unit |
|---|---|---|---|---|
| $\mathrm{SPA}$ | symmetric | commutative; Jordan; flexible; power-associative | associative; alternative | $e_0$ two-sided |
| $\mathrm{APA}$ | antisymmetric, alternating | Jacobi; flexible; power-associative | associative; commutative; alternative; unit | none |
| $\mathrm{GQA}$ | neither | left unit | associative; commutative; flexible; power-associative; alternative; right unit | $e_0$ left only |

Two rows of the table are read at once. **A symmetric product is flexible and power-associative**, because the two identities are read on the same argument twice and the symmetry interchanges the two readings; this gives the first row for $\mathrm{SPA}$. **An antisymmetric product is alternating, flexible and power-associative**, because $f(\tilde p,\tilde p)=-f(\tilde p,\tilde p)=0$ makes every square zero and the flexibility reads the antisymmetry once on each side; this gives the second row for $\mathrm{APA}$, and it makes the cubes zero. The general quaternionic product has the left unit $e_0$ alone, since $e_0^{\natural}\tilde q=\tilde q$ while $\tilde q^{\natural}e_0=\tilde q^{\natural}$, and it fails the remaining laws.

## The Two Laws of the Table

**Theorem (the two laws).** Among the three structures, the symmetric plain algebra is the only commutative one, and the antisymmetric plain algebra is the only one whose product satisfies the Jacobi identity.

*Proof.* The Jordan product is commutative by construction, and neither the cross product nor the general quaternionic product is: $\vec p\times\vec q=-\vec q\times\vec p$, while $\tilde p^{\natural}\tilde q$ and $\tilde q^{\natural}\tilde p$ differ in the vector part. The Jacobi identity, $\tilde p\wedge(\tilde q\wedge\tilde r)+\tilde q\wedge(\tilde r\wedge\tilde p)+\tilde r\wedge(\tilde p\wedge\tilde q)=0$, holds for the cross product because the cross product of vectors is the Lie bracket of the Lie algebra $\mathbb{R}^3=\mathfrak{so}(3)$; it fails for the general quaternionic product, whose cyclic sum on $(e_0,e_1,e_2)$ is $e_3\neq0$. None of the three is associative: associativity fails for the Jordan product on $(e_1,e_1,e_2)$, where the associator is $-e_2$; for the cross product on the same triple, where the associator is $+e_2$; and for the general quaternionic product on $(e_1,e_1,e_1)$, as in *Comparison Between the Two General Products*. Both statements are decided on the basis triples alone.

The two laws are the two rows of the menu that isolate two of the three companion structures, and they are the reason the category speaks of a Jordan layer and a Lie layer. The cross product is the only one of the three that is a Lie bracket; the Jordan product is the only commutative one; the general quaternionic product carries no law beyond the left unit.

## The Reading of the Three Structures

The blocks that follow read each of the three structures in turn. The general quaternionic algebra is *Introduction to the General Quaternionic Algebra*; the symmetric plain algebra is *Introduction to the Symmetric Plain Algebra*; and the antisymmetric plain algebra is *Introduction to the Antisymmetric Plain Algebra*. The algebra product itself, with its unit, its norm and its element theory, is *Introduction to the Quaternion Algebra* in the *Quaternions* category. Each of the three articles reads the product of the structure as a multiplication, with its own units, its own zero divisors and its own classes of element, using the vocabulary of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

**Remark (the same space, three times).** The three structures are not three algebras in the sense of three different vector spaces: they are one space with three companion products, and the vocabulary of the category is indexed by the product and not by the space. An element may be a unit for the algebra product and not for $\mathrm{SPA}$, a zero divisor for $\mathrm{SPA}$ and not for the algebra product, and every element is a square-zero element for $\mathrm{APA}$ and for it alone.

## Summary

The quaternion space carries three companion algebraic structures on the same four-dimensional real support, named once here: the symmetric plain algebra $\mathrm{SPA}$ with the Jordan product, the antisymmetric plain algebra $\mathrm{APA}$ with the cross product and the general quaternionic algebra $\mathrm{GQA}$ with the quaternionic product. Their structures are a commutative Jordan algebra with the unit $e_0$, a Lie algebra without unit and a non-associative left-unital algebra. The algebra product that makes the space a division algebra is not one of the three companion structures; it belongs to the *Quaternions* category.

The law table separates them: the symmetric product is commutative, flexible and power-associative; the antisymmetric product is alternating, flexible and power-associative, with cubes zero; the general quaternionic product has a left unit alone and fails associativity, commutativity, flexibility and power-associativity. The two laws of the table are that the symmetric plain algebra is the only commutative one and the antisymmetric plain algebra the only one satisfying Jacobi.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SPA}$ | symmetric plain algebra, the Jordan algebra of $\tilde p\bullet\tilde q$ |
| $\mathrm{APA}$ | antisymmetric plain algebra, the Lie algebra of $\tilde p\wedge\tilde q=\vec p\times\vec q$ |
| $\mathrm{GQA}$ | general quaternionic algebra, the left-unital rule $\tilde p^{\natural}\tilde q$ |
| support | the space $\mathbb{H}$, of real dimension four, for all three |
| the two laws | only $\mathrm{SPA}$ commutative; only $\mathrm{APA}$ satisfying Jacobi |
| $\tilde p\tilde q$ | the algebra product, of the *Quaternions* category |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan product, its identities and the algebra it defines.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Jacobi identity, the alternating bracket and the Lie algebra of the cross product.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for associativity, the unit and the symmetrisation of a bilinear product.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the products of the quaternion space and their companion algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the place of the cross product and the quaternion product among the Clifford products.
