# __The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

This article reads the twelve products of *The 12 Products of the Biquaternion Complex Space* as the algebraic structures they define, and gives each structure its three-letter name, the abbreviations being read with the table of the twelve.

Every one of the twelve products equips the complex space with an **algebraic structure**: its operation is the multiplication of a structure of its own kind, and the structure is read off the laws of that operation, which the table of *The 12 Products of the Biquaternion Complex Space* collects. The general product of a family is the multiplication of the **algebra** or the **sesqualgebra** of that family — the two bilinear families are the two algebras over $\mathbb{C}$ and the two sesquilinear families the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$ — and the symmetric part of each product is the multiplication of a **commutative** structure and its antisymmetric part the multiplication of an **alternating** one, the symmetry being up to the coefficientwise conjugation in the two sesquilinear families.

The name has three letters and is read as a code.

- The **first** letter says which of the three operations of a family is meant: $\mathrm G$ the **general** product, the multiplication itself, $\mathrm S$ its **symmetric** part, $\mathrm A$ its **antisymmetric** part.
- The **second** letter says which of the two products of the family is meant: $\mathrm P$ the **plain** one and $\mathrm Q$ the **quaternionic** one, in the sense of the first slot, read as it stands for $\mathrm P$ and through the natural conjugation ${}^{\natural}$ for $\mathrm Q$.
- The **third** letter says the **family**: $\mathrm A$ the algebra over $\mathbb{C}$, whose second slot is read as it stands, and $\mathrm S$ the sesqualgebra over $\mathbb{C}$, whose second slot carries the Hermitian conjugation ${}^{*}$.

The twelve names are these:

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

Each row is one family — the two algebras over $\mathbb{C}$ and the two sesqualgebras — and the three names of a row are the three structures of the family: the general structure of the family and its symmetrisation and its antisymmetrisation.

The four codes that begin with $\mathrm G$ name the four structures the corpus already names apart: $\mathrm{GPA}$ is the multiplication of *Introduction to the General Plain Algebra of Biquaternions*, $\mathrm{GQA}$ of *Introduction to the General Quaternionic Algebra of Biquaternions*, $\mathrm{GPS}$ of *Introduction to the General Plain Sesqualgebra of Biquaternions*, and $\mathrm{GQS}$ of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. The other eight codes are the symmetrisations and the antisymmetrisations of those four, and the body of *The 12 Products of the Biquaternion Complex Space* is where they are read.

**What the last letter does and does not claim.** Only the six structures whose code ends in $\mathrm A$ are algebras over $\mathbb{C}$: the three operations of the plain row and the three of the quaternionic row are $\mathbb{C}$-bilinear, so each is an algebra multiplication in the broad sense. The six whose code ends in $\mathrm S$ are the six operations of the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$: the two general ones, $\mathrm{GPS}$ and $\mathrm{GQS}$, are the multiplications of the two sesqualgebras over $\mathbb{C}$, and their four parts $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$ are sesquilinear again, because the exchange that splits them carries the conjugation of the value and keeps the class. The bare interchange of the two arguments, which returns a product of the **opposite** parity, has its own two halves — the symmetrised sesquilinear product and the sesquilinear commutator — and those are the only $\mathbb{R}$-bilinear operations of the family. The trailing $\mathrm S$ names the class of the operation, which is the class of the parent product, and it is read that way throughout. The twelve names are read against the class-preserving exchange; §*The Exchange Behind the Split* of *The 12 Products of the Biquaternion Complex Space* contrasts it with the bare interchange.

**Remark (one collision).** In the physics part of the corpus the letters $\mathrm{APS}$ also denote the *algebra of physical space*, the paravector space $\mathrm{span}_{\mathbb{R}}\{e_0,\gamma_k\}$ of *Paravectors and the Geometry of Spacetime*. In this article and its siblings the same letters denote $\mathrm{APS}$, the antisymmetric plain sesqualgebra, and the two readings occur in different parts of the corpus.

The article of each structure is its own: *Introduction to the Symmetric Plain Algebra of Biquaternions* for $\mathrm{SPA}$ and *Introduction to the Antisymmetric Plain Algebra of Biquaternions* for $\mathrm{APA}$; *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* and *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* for $\mathrm{SQA}$ and $\mathrm{AQA}$; *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* and *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* for $\mathrm{SPS}$ and $\mathrm{APS}$; and *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* and *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* for $\mathrm{SQS}$ and $\mathrm{AQS}$. Each of those articles names the product of its structure in the same sentence.

## The Twelve Structures, One by One

Each structure is read with its product, written on the coordinates, and with its decomposition: the scalar part and the vector part of the value, and, for the four general products, the split into their two parts. The notation is that of *The 12 Products of the Biquaternion Complex Space*.

### The General Plain Algebra (GPA)

Its product is the **general plain bilinear product**,
$$
\tilde{P}\tilde{Q}=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}.
$$
Its decomposition is the scalar part $P_0Q_0-(\mathbf{P},\mathbf{Q})$ and the vector part $P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$, and it splits into its two parts, $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$. The multiplication is associative, $e_0$ is a unit on both sides, and the values fill the whole space.

### The Symmetric Plain Algebra (SPA)

Its product is the **symmetric plain bilinear product**, the symmetric part of the general plain bilinear product.
$$
\tfrac12\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr)=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}.
$$
Its decomposition is the scalar part $P_0Q_0-(\mathbf{P},\mathbf{Q})$ and the vector part $P_0\mathbf{Q}+Q_0\mathbf{P}$. The multiplication is commutative and satisfies the Jordan identity, $e_0$ is a unit on both sides, and the values fill the whole space.

### The Antisymmetric Plain Algebra (APA)

Its product is the **antisymmetric plain bilinear product**, the antisymmetric part of the general plain bilinear product.
$$
\tfrac12\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr)=\mathbf{P}\times\mathbf{Q}.
$$
Its decomposition is the scalar part $0$ and the vector part $\mathbf{P}\times\mathbf{Q}$ alone. The multiplication is alternating and satisfies the Jacobi identity, it has no unit, and its values lie in the vector subspace.

### The General Quaternionic Algebra (GQA)

Its product is the **general quaternionic bilinear product**,
$$
\tilde{P}^{\natural}\tilde{Q}=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$
Its decomposition is the scalar part $P_0Q_0+(\mathbf{P},\mathbf{Q})$ and the vector part $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, and it splits into its two parts, $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$. The multiplication is not associative, $e_0$ is a unit on the left only, and the values fill the whole space.

### The Symmetric Quaternionic Algebra (SQA)

Its product is the **symmetric quaternionic bilinear product**, the symmetric part of the general quaternionic bilinear product.
$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr)=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr].
$$
Its decomposition is the scalar part $P_0Q_0+(\mathbf{P},\mathbf{Q})$ alone, its vector part being zero. The multiplication is commutative, it is not a Jordan product, its values lie in the centre, and it has no unit.

### The Antisymmetric Quaternionic Algebra (AQA)

Its product is the **antisymmetric quaternionic bilinear product**, the antisymmetric part of the general quaternionic bilinear product.
$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}\bigr)=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$
Its decomposition is the scalar part $0$ and the vector part $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$. The multiplication is alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace.

### The General Plain Sesqualgebra (GPS)

Its product is the **general plain sesquilinear product**,
$$
\tilde{P}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$
Its decomposition is the scalar part $P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ and the vector part $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$, and it splits into its two parts, $\mathrm{GPS}=\mathrm{SPS}+\mathrm{APS}$. The multiplication is sesquilinear over $(\mathbb{C},\bar{\cdot})$, it is not associative, $e_0$ is a unit on the right only, and the values fill the whole space.

### The Symmetric Plain Sesqualgebra (SPS)

Its product is the **symmetric plain sesquilinear product**, the symmetric part of the general plain sesquilinear product.
$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr].
$$
Its decomposition is the scalar part $P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ alone, its vector part being zero. The multiplication is conjugate-commutative, its values lie in the centre, and it has no unit.

### The Antisymmetric Plain Sesqualgebra (APS)

Its product is the **antisymmetric plain sesquilinear product**, the antisymmetric part of the general plain sesquilinear product.
$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$
Its decomposition is the scalar part $0$ and the vector part $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$. The multiplication is conjugate-alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace.

### The General Quaternionic Sesqualgebra (GQS)

Its product is the **general quaternionic sesquilinear product**,
$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}.
$$
Its decomposition is the scalar part $P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ and the vector part $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$, and it splits into its two parts, $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$. The multiplication is sesquilinear over $(\mathbb{C},\bar{\cdot})$, it is not associative, it has a unit on neither side, and the values fill the whole space.

### The Symmetric Quaternionic Sesqualgebra (SQS)

Its product is the **symmetric quaternionic sesquilinear product**, the symmetric part of the general quaternionic sesquilinear product.
$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}.
$$
Its decomposition is the scalar part $P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ and the vector part $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$. The multiplication is conjugate-commutative, it is not a Jordan product, it has no unit, and its values lie in no subspace of the remarkable subspaces.

### The Antisymmetric Quaternionic Sesqualgebra (AQS)

Its product is the **antisymmetric quaternionic sesquilinear product**, the antisymmetric part of the general quaternionic sesquilinear product.
$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}.
$$
Its decomposition is the scalar part $0$ and the vector part $\mathbf{P}\times\overline{\mathbf{Q}}$. The multiplication is conjugate-alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace.

### The Two That Are Lie and Jordan Products

Of the twelve, exactly two structures carry the product of one of the two classical nonassociative algebras, and both belong to the plain family. A symmetrisation is a **Jordan** product only when it satisfies the Jordan identity, an antisymmetrisation a **Lie** product only when it satisfies the Jacobi identity, and of the twelve exactly one of each meets its identity. The two are these:

- $\mathrm{APA}$ is alternating and satisfies the Jacobi identity, so its product is a **Lie** product; it is the Lie algebra of *The Unitary Lie Algebra*, with the vector subspace as a Lie subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, the quaternion subspace as $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace as $\mathfrak{u}(2)$, whose derived algebra is $\mathfrak{su}(2)$ (*Remarkable Subspaces and the Four General Products*).
- $\mathrm{SPA}$ is commutative and satisfies the Jordan identity, so its product is a **Jordan** product; it is the special Jordan algebra of degree two, and its Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$.

The other six parts fail the identity of their kind, and each failure is witnessed on a single triple or a single element:

| name | identity | witness | failure |
|---|---|---|---|
| $\mathrm{AQA}$ | Jacobi | $(e_0,e_1,e_2)$ | $-e_3$ |
| $\mathrm{APS}$ | Jacobi | $(e_0,e_1,e_2)$ | $e_3$ |
| $\mathrm{AQS}$ | Jacobi | $(e_1,e_1,ie_2)$ | $-2ie_2$ |
| $\mathrm{SQA}$ | Jordan | $x=y=e_1$ | the sides are $0$ and $e_0$ |
| $\mathrm{SPS}$ | Jordan | $x=y=e_1$ | the sides are $0$ and $e_0$ |
| $\mathrm{SQS}$ | Jordan | $x=y=e_1$ | the sides are $-e_0$ and $e_0$ |

The last column of the three Jacobi rows is the cyclic sum declared in the Conventions of *The 12 Products of the Biquaternion Complex Space*.

The three Jacobi failures have three different reasons. For $\mathrm{AQA}$ the culprit is the non-associativity of the product it comes from; for $\mathrm{APS}$ and $\mathrm{AQS}$ it is the obstruction of *Lie Algebras of Sesqualgebras*, where the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, which a genuine sesqualgebra forbids. The three Jordan failures are witnessed above, the first two on the same element $e_1$ because the two products agree on the real basis. In the three Jordan rows the last column gives the two sides of the identity, $(x^{2}\bullet x)\bullet x$ and $x^{2}\bullet(x\bullet x)$: they differ by $e_0$ for $\mathrm{SQA}$ and $\mathrm{SPS}$, whose symmetric square on $e_1$ is $e_0$, and by $2e_0$ for $\mathrm{SQS}$, whose symmetric square on $e_1$ is $-e_0$.

The four general products are neither symmetrisations nor antisymmetrisations, and neither identity is put to them: $\mathrm{GPA}$ is the one of the twelve whose product is associative, and the products of the other three are not associative.

---

## Summary

The twelve structures are the twelve products of *The 12 Products of the Biquaternion Complex Space* read as multiplications, and each name is three letters: the part, $\mathrm G$ general or $\mathrm S$ symmetric or $\mathrm A$ antisymmetric; the first slot, $\mathrm P$ plain or $\mathrm Q$ quaternionic; the family, $\mathrm A$ the algebra over $\mathbb{C}$ or $\mathrm S$ the sesqualgebra over $\mathbb{C}$. The four names that begin with $\mathrm G$ are the four structures the corpus names apart, the multiplications of the four general products, and the other eight are their symmetrisations and antisymmetrisations.

Of the twelve, two are the product of a classical nonassociative algebra and both belong to the plain family: $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ is the one Lie product and $\mathrm{SPA}=\tilde{P}\bullet\tilde{Q}$ the one Jordan product. The other six parts fail the identity of their kind, with the witnesses recorded above. The six structures whose code ends in $\mathrm A$ are $\mathbb{C}$-bilinear and the six whose code ends in $\mathrm S$ are sesquilinear over $(\mathbb{C},\bar{\cdot})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm G$, $\mathrm S$, $\mathrm A$ (first letter) | the general product, its symmetric part, its antisymmetric part |
| $\mathrm P$, $\mathrm Q$ (second letter) | the plain first slot, the quaternionic first slot |
| $\mathrm A$, $\mathrm S$ (third letter) | the family: the algebra over $\mathbb{C}$, the sesqualgebra over $\mathbb{C}$ |
| $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$ | the six structures of the two algebras over $\mathbb{C}$ |
| $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | the six structures of the two sesqualgebras over $\mathbb{C}$ |
| $B(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ | the quaternion form, the scalar part of $\mathrm{SQA}$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| Jacobi, Jordan | the two identities that single out $\mathrm{APA}$ and $\mathrm{SPA}$ |
| $\overline{\mathbf{Q}}$, $(\mathbf{P},\mathbf{Q})$, $\mathbf{P}\times\mathbf{Q}$ | the coefficientwise conjugate of the vector part, the bilinear dot product and the bilinear cross product |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, for the vocabulary the twelve are studied with: the classes of elements and the derived operations defined once for a general product and read on the products of the space.
- *The 12 Products of the Biquaternion Complex Space*, for the products themselves, the method of the decomposition and the table of the twelve with their laws, units and images.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, for the four general products that the four $\mathrm G$-names read as multiplications.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the two definitions of the split and the class-preserving exchange.
- *Introduction to the General Plain Algebra of Biquaternions*, *Introduction to the General Quaternionic Algebra of Biquaternions*, *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, for the four structures the corpus names apart; and the eight articles of the parts, *Introduction to the Symmetric Plain Algebra of Biquaternions* and its siblings, for the symmetrisations and antisymmetrisations.
- *Lie Algebras of Sesqualgebras*, for the obstruction that fails the Jacobi identity of the two sesquilinear antisymmetrisations, and *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra* for the two structures that pass.
