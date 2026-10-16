# __The Twelve Products and the Twelve Algebraic Structures__

## Introduction

The biquaternion complex space carries four general products, and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that one algebra carries **twelve products** and, with them, twelve algebraic structures. This article is the second of the three reader articles of the band *Focus on Biquaternioid structures*: the first reads the four general products and the four forms they carry, this one reads the twelve products the four split into and the structures they define, and the third reads the four forms and the four algebraic norms on the remarkable subspaces and under the change of scalars.

The article owns none of the twelve. The products, their laws, their units and their images are the matter of *The 12 Products of the Biquaternioid Complex Space*; the names and the structure each product defines are *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the classes — the product-relative unit, inverse, zero divisor, idempotent, nilpotent, square and form-theoretic class — are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; and each of the twelve has a band of its own in this menu, whose article reads its product and its physical job.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central $i$ with $i^{2}=-1$; a general element is $\tilde Q=Q_0e_0+\vec Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with complex coefficients $Q_\mu$ and vector part $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$, the coefficientwise conjugation $\bar{\cdot}$ conjugates the coefficients, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the scalar part is $\mathrm{Sc}$, the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$, and $(\vec P,\vec Q)$ and $\vec P\times\vec Q$ are the complex bilinear dot and cross products. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces and the two sectors $\mathbb{M}_+$, $\mathbb{M}_-$. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Method of the Split

Every general product is split into a symmetric and an antisymmetric part, and the split is a different operation in the two families of products. The two definitions agree on the reconstruction, on the symmetry of the two parts and on their uniqueness; they differ in the exchange that produces them.

**The bilinear case.** The general plain bilinear product and the general quaternionic bilinear product have two $\mathbb{C}$-linear slots, and the exchange is the plain interchange of the arguments,

$$
f^{\mathrm{s}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)+f(\tilde Q,\tilde P)\bigr),
\qquad
f^{\mathrm{a}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)-f(\tilde Q,\tilde P)\bigr).
$$

**The sesquilinear case.** The general plain sesquilinear product and the general quaternionic sesquilinear product have one linear and one conjugate-linear slot, and the interchange alone returns a product of the opposite type, which is not a product of the class at all. The exchange is the **conjugate transpose**, the interchange followed by the coefficientwise conjugation of the value,

$$
f^{\mathrm{s}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)+\overline{f(\tilde Q,\tilde P)}\bigr),
\qquad
f^{\mathrm{a}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)-\overline{f(\tilde Q,\tilde P)}\bigr).
$$

**Why the exchange is adapted.** The exchange is chosen so that both parts are operations of the **same class as the product they split** — $\mathbb{C}$-bilinear in the two bilinear families and sesquilinear over $(\mathbb{C},\bar{\cdot})$ in the two sesquilinear ones — and this class-preservation is the reason the sesquilinear split is the conjugate transpose and not the bare interchange. The bare interchange of a sesquilinear product has two halves that are only $\mathbb{R}$-bilinear, the symmetrised sesquilinear product and the sesquilinear commutator, and they are not the two parts read here; the twelve names are read against the class-preserving exchange.

**What the two cases share, and where they part.** Both parts satisfy $f=f^{\mathrm{s}}+f^{\mathrm{a}}$; the symmetric part is fixed by the exchange, the antisymmetric part negated by it, and the pair is unique. In the **bilinear case** the antisymmetric part vanishes at the two equal arguments, so the square is the symmetric part alone and the polarisation of the square recovers the symmetric part away from the two equal arguments. In the **sesquilinear case** the antisymmetric part at the two equal arguments is the antisymmetrised square, $f^{\mathrm{a}}(\tilde Q,\tilde Q)=\tfrac12\bigl(f(\tilde Q,\tilde Q)-\overline{f(\tilde Q,\tilde Q)}\bigr)$, which need not vanish; the square is split by the exchange, and the antisymmetric side is the conjugate half-difference of the square. That half-difference is the vector part of the square in the **plain** sesquilinear family, whose square $\tilde Q\tilde Q^{*}$ is Hermitian, and it is no longer the vector part of the square in the **quaternionic** family, whose square $\tilde Q^{\natural}\tilde Q^{*}$ is not; there the algebraic norm is the single conjugate cross product $\vec Q\times\overline{\vec Q}$. The two sesquilinear families cannot therefore be quoted with one formula for the algebraic norm. The polarisation of the square recovers the **plain** symmetrisation and not the symmetric part. The bilinear case has no antisymmetric algebraic norm; the sesquilinear case has one, and it is not zero in general.

## The Twelve Products

Each of the four general products is read with its two parts, the symmetric and the antisymmetric one. The four general products come first, then their four symmetric parts, then their four antisymmetric parts; inside each group the plain algebra, then the plain sesqualgebra, then the quaternionic algebra, then the quaternionic sesqualgebra.

| code | name | product | scalar part | vector part |
|---|---|---|---|---|
| $\mathrm{GPA}$ | the general plain bilinear product | $\tilde P\tilde Q$ | $P_0Q_0-(\vec P,\vec Q)$ | $+P_0\vec Q+Q_0\vec P+\vec P\times\vec Q$ |
| $\mathrm{GPS}$ | the general plain sesquilinear product | $\tilde P\tilde Q^{*}$ | $P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q}$ |
| $\mathrm{GQA}$ | the general quaternionic bilinear product | $\tilde P^{\natural}\tilde Q$ | $P_0Q_0+(\vec P,\vec Q)$ | $+P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ |
| $\mathrm{GQS}$ | the general quaternionic sesquilinear product | $\tilde P^{\natural}\tilde Q^{*}$ | $P_0\overline{Q_0}-(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}-\overline{Q_0}\vec P+\vec P\times\overline{\vec Q}$ |
| $\mathrm{SPA}$ | the symmetric plain bilinear product | $\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)$ | $P_0Q_0-(\vec P,\vec Q)$ | $+P_0\vec Q+Q_0\vec P$ |
| $\mathrm{SPS}$ | the symmetric plain sesquilinear product | $\tfrac12\bigl(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural}\bigr)$ | $P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | $0$ |
| $\mathrm{SQA}$ | the symmetric quaternionic bilinear product | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)$ | $P_0Q_0+(\vec P,\vec Q)$ | $0$ |
| $\mathrm{SQS}$ | the symmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)$ | $P_0\overline{Q_0}-(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}-\overline{Q_0}\vec P$ |
| $\mathrm{APA}$ | the antisymmetric plain bilinear product | $\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)$ | $0$ | $\vec P\times\vec Q$ |
| $\mathrm{APS}$ | the antisymmetric plain sesquilinear product | $\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q}\tilde P^{\natural}\bigr)$ | $0$ | $-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q}$ |
| $\mathrm{AQA}$ | the antisymmetric quaternionic bilinear product | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)$ | $0$ | $P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ |
| $\mathrm{AQS}$ | the antisymmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)$ | $0$ | $\vec P\times\overline{\vec Q}$ |

Two remarks fix the table. The **symmetrisation keeps the scalar part** of the general product unchanged and the **antisymmetrisation keeps the vector part**: for each family the general product and its symmetric part share one scalar part, and the general product and its antisymmetric part share one vector part. In the **plain sesquilinear** family the conjugate transpose of the value is its natural conjugate, so the antisymmetric part is the vector part of the single value $f(\tilde P,\tilde Q)$; in the **quaternionic sesquilinear** family the two orders are not conjugate values and the two parts are the half-sum and the half-difference of the two orders, which is why the values of $\mathrm{SQS}$ lie in no remarkable subspace.

## The Twelve Algebraic Structures

Every one of the twelve products equips the complex space with an algebraic structure, and the structure is read off the laws of the operation. The general product of a family is the multiplication of the **algebra** or the **sesqualgebra** of that family, and the symmetric part of each product is the multiplication of a commutative structure and its antisymmetric part the multiplication of an alternating one, the symmetry being up to the coefficientwise conjugation in the two sesquilinear families. The code has three letters and the structure carries a name beside it: the first letter of the code says which of the three operations of the family — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one; the third says the family — $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra over $(\mathbb{C},\bar{\cdot})$. The names are these, the operation — *general*, *symmetric* or *antisymmetric* — put in front of the name of the family.

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | the general plain algebra ($\mathrm{GPA}$) | the symmetric plain algebra ($\mathrm{SPA}$) | the antisymmetric plain algebra ($\mathrm{APA}$) |
| the plain sesqualgebra | the general plain sesqualgebra ($\mathrm{GPS}$) | the symmetric plain sesqualgebra ($\mathrm{SPS}$) | the antisymmetric plain sesqualgebra ($\mathrm{APS}$) |
| the quaternionic algebra | the general quaternionic algebra ($\mathrm{GQA}$) | the symmetric quaternionic algebra ($\mathrm{SQA}$) | the antisymmetric quaternionic algebra ($\mathrm{AQA}$) |
| the quaternionic sesqualgebra | the general quaternionic sesqualgebra ($\mathrm{GQS}$) | the symmetric quaternionic sesqualgebra ($\mathrm{SQS}$) | the antisymmetric quaternionic sesqualgebra ($\mathrm{AQS}$) |

Only the six structures whose code ends in $\mathrm A$ are algebras over $\mathbb{C}$: the three operations of the plain row and the three of the quaternionic row are $\mathbb{C}$-bilinear, so each is an algebra multiplication in the broad sense. The six whose code ends in $\mathrm S$ are the six operations of the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$, and their four parts are sesquilinear again because the exchange that splits them carries the conjugation of the value. The four codes that begin with $\mathrm G$ name the four structures the corpus already names apart; the other eight are their symmetrisations and antisymmetrisations.

The twelve together have three patterns, and they are the patterns a reader compares them by. The **units** are carried by four structures and no others: the two-sided unit $e_0$ by the two plain bilinear structures $\mathrm{GPA}$ and $\mathrm{SPA}$, the right unit by the general plain sesquilinear product $\mathrm{GPS}$, and the left unit by the general quaternionic product $\mathrm{GQA}$. The **images** fall into four classes: the whole space for the four general products and $\mathrm{SPA}$, the centre for the two central-valued symmetric parts $\mathrm{SPS}$ and $\mathrm{SQA}$, the vector subspace for the four antisymmetric parts, and no remarkable subspace for $\mathrm{SQS}$. The **forms** are carried by eight of the twelve and by no antisymmetric part: the general and symmetric member of each family carries the form of the family, and the four antisymmetric parts carry no form and measure nothing.

## Which Identities Survive

Each structure is asked for the law of its kind: associativity for a general product, (conjugate-)commutativity for a symmetric part, (conjugate-)alternation for an antisymmetric part. Over and above those, the two classical identities single out exactly one structure of each kind, and the twelve are mostly the account of the others failing.

**The Jacobi identity**, asked of the four antisymmetric parts, holds for $\mathrm{APA}$ alone — the antisymmetric plain product is the cross product $\vec P\times\vec Q$, the Lie bracket of the rotation algebra — and fails for the other three. Its failure is densest for $\mathrm{APS}$, failing on half the triples, and sparsest for $\mathrm{AQS}$, whose witness needs a complex element: on the eight-element real basis $\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$ the failing triples number none for $\mathrm{APA}$, $252$ for $\mathrm{APS}$, $144$ of $512$ for $\mathrm{AQA}$ and $72$ for $\mathrm{AQS}$.

**The Jordan identity**, asked of the four symmetric parts, holds for $\mathrm{SPA}$ alone — the symmetrisation of the plain product, the product of the Jordan algebra of the observables — and fails for the other three: $\mathrm{SPS}$ fails at $7$ of the $8$ basis elements, $\mathrm{SQA}$ at $6$ and $\mathrm{SQS}$ at $4$. The failures of the three are of two shapes, the central shift of $\mathrm{SQS}$ and the outright vanishing of $\mathrm{SPS}$ and $\mathrm{SQA}$, and a shift needs a product with a non-central algebraic norm, which is the mark of the sesquilinear block.

**Two cautions.** The counts are counts on a chosen basis and are not invariants of the operation; they are given as the shape of each failure and they change with the basis. And the identity is tested in the single form the corpus declares, the Jordan identity in its two-variable form and read at $y=x$ as the corpus's witnesses do. Neither identity is put to the four general products, which are neither symmetrisations nor antisymmetrisations; each is put to the four parts of its kind.

## The Definitions the Twelve Need

The vocabulary the twelve structures are read with — unit, inverse, zero divisor and annihilator, idempotent, projection and Peirce decomposition, nilpotent, power and square root, derived operation and form-theoretic class — is **product-relative**. A unit is a unit in the product in force, an inverse an inverse there, a zero divisor a zero divisor there; the same element may be a unit in one of the twelve and a zero divisor in another, and neither statement needs the other to be false. The general definitions, the transport of a class along an isomorphism and the dictionary between the classes and the four general products are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, and they are the vocabulary every band article uses.

Two facts of the definitional layer matter for the band. The four general products **coincide on one of the element classes they decide**: the four zero-divisor sets are one set, because they are governed by the same central square $C(\tilde P)=\sum_\mu P_\mu^{2}$; the annihilators, the squares, the idempotents and the units are product-dependent and do not coincide. And the classes are read on the **whole** complex space unless a subspace is named, since the count of twelve is the count for the complex space and a computation on a real form sees ten.

## The Twelve on the Real Forms: Twelve to Ten

The twelve operations are pairwise distinct on the complex space, but on the **real part** — the real span of $e_0,e_1,e_2,e_3$, where the coefficientwise conjugation fixes every element — two pairs coincide, and the twelve fall to **ten**:

$$
\mathrm{SPS}=\mathrm{SQA}
\qquad\text{and}\qquad
\mathrm{APA}=\mathrm{AQS}
\qquad\text{on the real part.}
$$

The first coincidence is the equality of the two scalar forms of the pair, $N=H$ on the real elements; the second is the equality of the two cross products on real vectors. A third distinction also disappears: the Jacobi failure of $\mathrm{AQS}$, whose witness is $(e_1,e_1,ie_2)$ and needs a complex element, is invisible on the real forms, so the parity of $\mathrm{APA}$ and $\mathrm{AQS}$, which the Jacobi identity separates on the complex space, is not separated on the real one.

**Caution.** The fall from twelve to ten is a loss of distinctions, and it is exact: a computation restricted to real elements cannot separate the members of either coincident pair, and a property that holds for one member and fails for the other is invisible there. A reader who checks an identity — an associativity, a Jacobi or a Jordan condition — on real elements only therefore risks reporting an obstruction as absent, or a structure as present, when the distinction between the two members of a coincident pair has simply been erased by the reality condition. The twelve are the objects of the complex space; a real form carries ten of them. The physical reading of the fall is *The Biquaternioid Antisymmetric Quaternionic Sesqualgebra (AQS) over $\mathbb{C}$*.

## Physical Readings

The twelve structures are one algebra read in twelve products, and the reading places each structure by its product, its law and its form.

**By product**, the four families are the four jobs of *The Four General Products and the Degree-2 Forms of the Biquaternion Space* — composition, probability, causality and gauge — and within a family the general product is the operation, the symmetric part the half that measures or couples, and the antisymmetric part the half that orders, rotates or phases. **By law**, exactly two of the twelve are the product of a classical nonassociative algebra, the Jordan product $\mathrm{SPA}$ and the Lie product $\mathrm{APA}$, and they are the two the menu names commutativity and rotation. **By form**, the eight structures that carry a form split into the two that measure — the sector sign $\langle\tilde P,\tilde Q\rangle$ of the plain product, definite on each sector, and the positive definite $\langle\tilde P,\tilde Q\rangle_{*}$ of the plain sesquilinear product — and the two that carry a metric — the indefinite interval $\langle\cdot\rangle_{\natural}$ and the Krein form $\langle\tilde P,\tilde Q\rangle_{\natural*}$; the four antisymmetric parts carry no form and measure nothing.

The reading of the twelve side by side on the three axes is *The Twelve Structures Compared: Product, Law and Form*, and the same twelve read through the maps their elements define is *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*. Each of the twelve has its own entry in the menu, and each entry names the physical job of its structure; they are grouped in the band *Focus on Biquaternioid structures*.

## Summary

The four general products of the biquaternion complex space each split into a symmetric and an antisymmetric part, by the plain interchange in the two $\mathbb{C}$-bilinear families and by the conjugate transpose in the two sesquilinear families, so that the space carries **twelve products**. Each is the multiplication of an algebraic structure of its own kind, named by a three-letter code whose first letter is the operation, the second the product and the third the family, and the four families are the two algebras over $\mathbb{C}$ and the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$.

Of the twelve, exactly one general product is associative, the general plain product $\mathrm{GPA}$; exactly one symmetric part satisfies the Jordan identity, the plain $\mathrm{SPA}$; and exactly one antisymmetric part satisfies the Jacobi identity, the plain $\mathrm{APA}$. The other three symmetric parts and the other three antisymmetric parts fail the identity of their kind, with the witnesses and counts of the table, and the failure of $\mathrm{AQS}$ is invisible on the real forms. The units are carried by $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$ and $\mathrm{SPA}$ alone; the images are the whole space, the centre, the vector subspace, or no remarkable subspace for $\mathrm{SQS}$; and the forms are carried by eight of the twelve, the four antisymmetric parts carrying none. On the real part the twelve fall to ten, through $\mathrm{SPS}=\mathrm{SQA}$ and $\mathrm{APA}=\mathrm{AQS}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm G$, $\mathrm S$, $\mathrm A$ | the general product, its symmetric part, its antisymmetric part |
| $\mathrm P$, $\mathrm Q$ | the plain first slot, the quaternionic first slot |
| $\mathrm A$, $\mathrm S$ | the family: the algebra over $\mathbb{C}$, the sesqualgebra over $\mathbb{C}$ |
| $\mathrm{GPA},\mathrm{GQA},\mathrm{SPA},\mathrm{SQA},\mathrm{APA},\mathrm{AQA}$ | the six structures of the two algebras over $\mathbb{C}$ |
| $\mathrm{GPS},\mathrm{GQS},\mathrm{SPS},\mathrm{SQS},\mathrm{APS},\mathrm{AQS}$ | the six structures of the two sesqualgebras over $\mathbb{C}$ |
| $f^{\mathrm{s}}(\tilde P,\tilde Q)$, $f^{\mathrm{a}}(\tilde P,\tilde Q)$ | the symmetric and antisymmetric parts of a product |
| $\overline{f(\tilde Q,\tilde P)}$ | the conjugate transpose, the exchange of a sesquilinear product |
| Jordan, Jacobi | the two identities that single out $\mathrm{SPA}$ and $\mathrm{APA}$ |
| the eight-element basis | $\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$, the form on which the failures are counted |

## Further Reading

- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the method of the split, the products in coordinates, the table of the laws, the units and the images, and the counts of the failures.
- *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the three-letter names and the structure each product defines.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the product-relative classes and the dictionary between the classes and the four general products.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`) and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the two definitions of the split and the obstruction of the class.
- *The Twelve Structures Compared: Product, Law and Form* (`articles_physics/the-twelve-structures-compared-product-law-and-form.md`), for the twelve side by side on the product, the law and the form.
- *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), for the same twelve read through the maps their elements define.
- *The Biquaternioid Antisymmetric Quaternionic Sesqualgebra (AQS) over $\mathbb{C}$* (`articles_physics/the-biquaternioid-antisymmetric-quaternionic-sesqualgebra-aqs-over-c.md`), for the physical reading of the fall from twelve to ten.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions of the algebra and its subspaces.
- Companion articles *The Four General Products and the Degree-2 Forms of the Biquaternion Space* (`articles_physics/the-four-general-products-and-the-degree-2-forms-of-the-biquaternion-space.md`) and *The Four Forms, the Four Algebraic Norms and the Change of Scalars* (`articles_physics/the-four-forms-the-four-algebraic-norms-and-the-change-of-scalars.md`).
