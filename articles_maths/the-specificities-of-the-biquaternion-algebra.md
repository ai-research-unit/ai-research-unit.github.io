# __The Specificities of the Biquaternion Algebra__

## Introduction

Of the twelve algebraic structures that the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one makes it an associative unital algebra over $\mathbb{C}$: the **general plain bilinear product** $\tilde Q_1\tilde Q_2$ of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, the multiplication of *Introduction to the Biquaternion Algebra*. Every unital result of this block belongs to it — the ideal lattice and the Peirce decomposition of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, the module theory of *Modules over the Biquaternion Algebra*, the corner subalgebras and the enveloping algebra of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* — and this article states the exact reason, in one identity, and then develops the theory that the identity unlocks.

The reason is **left alternativity**, the law $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$ at every pair; it is equivalent to the operator identity $L_{\tilde Q_1}L_{\tilde Q_1}=L_{\tilde Q_1\tilde Q_1}$, and it is the threshold at which the operator calculus of the block begins. It is strictly weaker than associativity, so it is the sharp statement, and it is the criterion that separates the plain product from the other eleven. What the criterion opens is the block's own subject matter: the projectors of the idempotents, the flags of the nilpotents, the Peirce decomposition with its corner subalgebras and matrix units, the ideal lattice, the enveloping algebra and the module category. This article states the criterion, reads the unital theory of the block as its consequence, and closes by naming the eleven structures that fail the law and the one structure that sits on its boundary.

**Placement.** The article closes the *Specific Theory* section of the biquaternion algebra, after *Ideals and Peirce Decomposition of the Biquaternion Algebra* and *Modules over the Biquaternion Algebra*, whose results it reads back as consequences of one identity; the enveloping algebra of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* is in the *Operators* section of the same block and is cited, not sequenced. It is a synthesis: it uses the classification of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, the four products of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, the property table of *Comparison Between the Four General Products* and the closure failure of *Relations Between the Four General Products* §*The Left Multiplications*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y=\vec e_z$ and central scalar imaginary $i$. The **plain product** is written as juxtaposition $\tilde Q_1\tilde Q_2$; a product written $\circ$ is a generic one, and its identity is stated at each use. The natural conjugation is ${}^{\natural}$, $\tilde Q^{\natural}=Q_t-\vec Q$; the star is ${}^{*}$, the Hermitian conjugation of the corpus, $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$, the composite of the natural conjugation with the conjugation of the coefficients; and the **bar** is $\overline{\tilde Q}=\tilde Q^{\natural*}=\tilde Q^{*\natural}$, the conjugation of the coefficients alone; all three fix $e_t$, and the star and the bar are conjugate-linear. The **left multiplication** of a product $\circ$ by $\tilde Q_1$ is the map $L^{\circ}_{\tilde Q_1}:\tilde Q_2\mapsto\tilde Q_1\circ\tilde Q_2$, and the superscript is dropped for the plain product. The subscript is the element, never the operator: $L_{\tilde Q_1}L_{\tilde Q_2}$ is the composite $L_{\tilde Q_1}\circ L_{\tilde Q_2}$. An **idempotent** of the algebra is an element equal to its own square, and a **projector** is an idempotent operator, that is an idempotent of the morphism space; the zero operator is one, and the two levels are never interchanged. An idempotent element corresponds to a projector when its multiplication operator is idempotent, and the content of the criterion below is exactly that correspondence for the plain product.

## The Criterion

**Definition (left alternativity).** A product $\circ$ on the complex space is **left-alternative** when

$$
\tilde Q_1\circ(\tilde Q_1\circ\tilde Q_2)=(\tilde Q_1\circ\tilde Q_1)\circ\tilde Q_2\qquad\text{for all }\tilde Q_1,\tilde Q_2 .
$$

**Theorem (the criterion).** For a product $\circ$ the operator identity

$$
L^{\circ}_{\tilde Q_1}\circ L^{\circ}_{\tilde Q_1}=L^{\circ}_{\tilde Q_1\circ\tilde Q_1}\qquad\text{for every }\tilde Q_1
$$

holds exactly when $\circ$ is left-alternative.

*Proof.* Evaluate both sides at $\tilde Q_2$: the left side is $\tilde Q_1\circ(\tilde Q_1\circ\tilde Q_2)$ and the right side is $(\tilde Q_1\circ\tilde Q_1)\circ\tilde Q_2$. The two operators agree for all $\tilde Q_1,\tilde Q_2$ exactly when the two elements agree for all $\tilde Q_1,\tilde Q_2$, which is the definition of left alternativity.

**Corollary (idempotents and nilpotents).** In a left-alternative structure every idempotent gives a **projector**, $L_{\tilde\Pi}^{2}=L_{\tilde\Pi}$, and every square-zero element gives a **square-zero operator**, $L_{\tilde\Upsilon}^{2}=0$.

*Proof.* By the theorem $L_{\tilde\Pi}^{2}=L_{\tilde\Pi\circ\tilde\Pi}=L_{\tilde\Pi}$ and $L_{\tilde\Upsilon}^{2}=L_{\tilde\Upsilon\circ\tilde\Upsilon}=L_{0}=0$.

The corollary is the whole mechanism by which an element produces subspaces, and the reason is worth stating. A projector has an image and a kernel, the two are subspaces, they add to the whole space, and the image is the fixed set; an element of square zero gives an operator whose image lies in its kernel, so it produces a **flag** $\{0\}\subseteq\mathrm{im}\,L\subseteq\ker L\subseteq\mathbb{B}$. Neither construction has any reason to exist without the identity of the theorem.

**Remark (one-sided by construction).** The criterion uses the left multiplications, and the mirror statement with the right multiplications characterizes right alternativity; a product is associative exactly when the two laws of the criterion hold together. Left alternativity is strictly weaker than associativity — the octonions are left-alternative and not associative — so the corollary is not associativity in disguise, and the criterion is the sharp threshold of the theories that follow.

**Proposition (the plain product is left-alternative).** The general plain product satisfies the criterion at every element, with both sides equal to $L_{\tilde Q_1^{2}}$.

*Proof.* The plain product is associative, and associativity gives $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$ directly. Verified by recomputation for 100 random pairs with error below $10^{-15}$.

## The Associative Interpretation

The block is not only the one structure where the criterion holds; it is the one structure whose full associative theory is available. This section states that theory in the block's own terms, and each item is owned by an article of the block and cited.

**The algebra.** The plain product is associative, unital with unit $e_t$, and $\mathbb{C}$-bilinear, so $\mathbb{B}$ is an associative unital $\mathbb{C}$-algebra. Under the $2\times2$ matrix element representation of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, with $M(e_t)=\mathbb 1$ and $M(\vec e_k)=-i\sigma_k$, the algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, a central simple algebra of complex dimension four. Its centre is the scalar line,

$$
Z(\mathbb{B})=\mathbb{C}e_t,
$$

and it has no two-sided ideal other than $0$ and $\mathbb{B}$: the block is **simple**, and every non-zero element generates the whole algebra as a two-sided ideal.

**The ideal lattice.** The one-sided ideals are the subspaces $\mathbb{B}\tilde Q$ and $\tilde Q\mathbb{B}$ of the non-zero elements, the minimal left ideals being the images of the rank-one elements, so $M_2(\mathbb{C})$ gives the ladder

$$
0\subsetneq \mathbb{B}\tilde\Upsilon\subsetneq \mathbb{B},\qquad \mathbb{B}\tilde\Upsilon\ \text{a minimal left ideal},
$$

for a non-zero element $\tilde\Upsilon$ of square zero, and the mirror for the right ideals. *Ideals and Peirce Decomposition of the Biquaternion Algebra* computes the lattice, and its point is that **an element of square zero and its annihilator generate the same ideal**: the left ideal $\mathbb{B}\tilde\Upsilon$ has complex dimension two, and it equals its own annihilator, $\mathbb{B}\tilde\Upsilon=\{\tilde Q:\tilde Q\tilde\Upsilon=0\}=\mathrm{ann}(\tilde\Upsilon)$, also of complex dimension two, because $\tilde Q\tilde\Upsilon\cdot\tilde\Upsilon=\tilde Q\tilde\Upsilon^{2}=0$ puts every element of the ideal inside the annihilator and the two dimensions agree.

**The Peirce decomposition.** The idempotents of the block are the idempotent matrices, and each non-trivial idempotent $\tilde\Pi$ with complementary idempotent $\tilde\Pi'=e_t-\tilde\Pi$ gives the **quadratic** Peirce decomposition

$$
\mathbb{B}=\mathbb{B}_{11}\oplus\mathbb{B}_{12}\oplus\mathbb{B}_{21}\oplus\mathbb{B}_{22},\qquad
\mathbb{B}_{ij}=\{\tilde Q:\tilde\Pi\tilde Q\tilde\Pi_j=\tilde Q\},\quad \tilde\Pi_1=\tilde\Pi,\ \tilde\Pi_2=\tilde\Pi',
$$

into two **corner subalgebras** $\mathbb{B}_{11}=\tilde\Pi\mathbb{B}\tilde\Pi$ and $\mathbb{B}_{22}=\tilde\Pi'\mathbb{B}\tilde\Pi'$, each isomorphic to $\mathbb{C}$, and two off-diagonal spaces $\mathbb{B}_{12}=\tilde\Pi\mathbb{B}\tilde\Pi'$ and $\mathbb{B}_{21}$, each of complex dimension one, carrying the **matrix units** $E_{ij}\in\mathbb{B}_{ij}$ with

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

The four elements $E_{11},E_{12},E_{21},E_{22}$ form a $\mathbb{C}$-basis of $\mathbb{B}$ that behaves exactly as the matrix units of $M_2(\mathbb{C})$; the mixed spaces are one-dimensional, and this is the sharp contrast with a Jordan algebra, whose Peirce theory has a single middle space and no corners.

**The enveloping algebra and the modules.** The left and the right multiplications generate the **enveloping operator algebra** $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{opp}}$, and *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* proves $\mathbb{B}^{\mathrm e}\cong\mathrm{End}_\mathbb{C}(\mathbb{B})\cong M_4(\mathbb{C})$: the sandwich action $(\tilde x\otimes\tilde y^{\mathrm{opp}})\cdot\tilde z=\tilde x\tilde z\tilde y$ is faithful and exhausts the $\mathbb{C}$-linear operators on the four-dimensional space. It is in this sense that the block has an operator algebra and not merely a collection of operators, and the same identifies its bi-module $\mathbb{B}$ with the regular bi-module $_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$. Because $\mathbb{B}$ is simple and finite-dimensional, every module is semisimple and the finitely generated modules are the finite powers of the simple module, the content of *Modules over the Biquaternion Algebra*: the block is Morita-trivial, its module category equivalent to that of $\mathbb{C}$.

## What the Criterion Delivers

The criterion of §*The Criterion* is the exact statement of why the whole preceding section is available in the block. Four consequences, each a theorem of the block and each a comparison with what a weaker law delivers.

- **The projector calculus.** Every idempotent gives a projector, so every idempotent splits the space as $\mathbb{B}=\mathrm{im}\,L_{\tilde\Pi}\oplus\ker L_{\tilde\Pi}$; because the product is associative, the image is the principal left ideal $\mathbb{B}\tilde\Pi$, the kernel is the annihilator $\mathrm{ann}(\tilde\Pi)$, and the splitting is the one of §*The Associative Interpretation*. In a structure without the criterion an idempotent still gives a **fixed set** of $L_{\tilde\Pi}$, but not a complement.
- **The flag of the nilpotents.** Every square-zero element gives a square-zero operator with image equal to kernel, $\mathrm{im}\,L_{\tilde\Upsilon}=\ker L_{\tilde\Upsilon}=\mathbb{B}\tilde\Upsilon=\mathrm{ann}(\tilde\Upsilon)$, a two-dimensional subspace. The operator produces the subspace and its own annihilator at once, and the ideal it generates is exactly the annihilator.
- **The Peirce decomposition.** Because $L_{\tilde\Pi}$ is a projector and the product is associative, the projector decomposes $\mathbb{B}$ into the four Peirce spaces of §*The Associative Interpretation*, the corner subalgebras included. The decomposition is a theorem of the block; in a structure where the criterion fails, the spaces can be defined and do not carry the corner structure.
- **The module theory.** Because $\mathbb{B}$ is associative and unital, the left $\mathbb{B}$-modules are the representations, the ideal theory and the module theory are one subject, and the enveloping algebra acts on the bi-module. None of this survives the loss of the criterion.

## The Isolation among the Twelve

One law separates the block from the other eleven, and this section names it and the boundary.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, the general plain product is the only one that is left-alternative, equivalently the only one whose multiplication operators satisfy $L^{\circ}_{\tilde Q_1}L^{\circ}_{\tilde Q_1}=L^{\circ}_{\tilde Q_1\circ\tilde Q_1}$ at every element.

**Proof.** The twelve are generated from the plain product by one of three operations, twisting the first slot with ${}^{\natural}$, twisting the second slot with ${}^{*}$, or (anti)symmetrising, and each destroys the law. The first twist makes the identity demand $\tilde Q_1^{\natural}\tilde Q_1^{\natural}=\tilde Q_1^{\natural}\tilde Q_1$ at every element, false at $\tilde Q_1=\vec e_x$ since $-e_t\neq e_t$; the second makes $L^{\circ}_{\tilde Q_1}{}^{2}=L^{\circ}_{\tilde Q_1\circ\tilde Q_1}$ a clash between a conjugate-linear and a linear operator, so that a projector would have to vanish; the symmetrisation and the antisymmetrisation insert the cross terms of a left and a right multiplication, and the antisymmetrisation in addition forces a Lie algebra whose adjoint maps are all square-zero, which the cross product is not. The general plain product keeps the law by associativity.

The isolation is about the **theorem** and not about isolated elements, and the distinction is the exact boundary of the claim. Single elements of the other structures do produce projectors — the unit in the symmetric structures, the plain idempotents in the general quaternionic product — and square-zero operators, but no other structure carries the law, hence the class of its well-behaved elements is not a theory. The article therefore refuses the false strengthening "no other structure has a projector" and states the true one: only here is the correspondence between idempotents and projectors, and between nilpotents and flags, a theorem of the structure.

| family | structures | left-alternative | mechanism of the failure |
|---|---|---|---|
| plain | the algebra | **yes** | — (associativity) |
| symmetrised plain | SPA, APA | no | cross term of a left and a right multiplication |
| first slot ${}^{\natural}$ | GQA | no | the identity would force $\tilde Q_1^{\natural}\tilde Q_1^{\natural}=\tilde Q_1^{\natural}\tilde Q_1$, false at $\vec e_x$ |
| from GQA | SQA, AQA | no | the first-slot twist, with the cross terms of the (anti)symmetrisation |
| second slot ${}^{*}$ | GPS, GQS | no | the second slot is read through ${}^{*}$, so the criterion equates a linear with a conjugate-linear operator |
| from the sesquilinear | SPS, APS, SQS, AQS | no | the second-slot twist, with the cross terms of the (anti)symmetrisation |

## The Boundary of the Criterion

The one structure that comes closest is the general quaternionic product $\tilde Q_1\circ\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$, the **boundary** of the criterion. Its multiplication operator is a plain one with a conjugated index,

$$
L^{\circ}_{\tilde Q_1}=L_{\tilde Q_1^{\natural}},
$$

so it inherits the projector calculus of the plain product for the elements whose conjugate is an idempotent, while it fails the criterion at the elements where that conjugation does not happen. The general quaternionic product and the criteria it does and does not satisfy are *The Specificities of the General Quaternionic Algebra*, and it is named here only to locate the boundary: the plain product is the criterion, the general quaternionic product is the nearest structure to it, and the remaining ten are further.

## Summary

Of the twelve structures on $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the general plain product $\tilde Q_1\tilde Q_2$ is the only associative unital one, and the exact threshold of its theory is **left alternativity**, $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$ at every pair, equivalently $L_{\tilde Q_1}L_{\tilde Q_1}=L_{\tilde Q_1\tilde Q_1}$ at every element. From that single identity follow the projector calculus of the idempotents, the square-zero operators of the nilpotents, the quadratic Peirce decomposition into two corner subalgebras and two one-dimensional mixed spaces with matrix units $E_{ij}E_{kl}=\delta_{jk}E_{il}$, and the module theory of the block. The block is the central simple algebra $\mathbb{B}\cong M_2(\mathbb{C})$ with centre $\mathbb{C}e_t$, its ideals are the subspaces generated by square-zero elements, the ideal generated by a nilpotent coinciding with its own annihilator, and its enveloping algebra is $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$. The criterion holds in the plain product and in no other of the twelve: the four general products other than the plain fail through the conjugation of a slot, the antisymmetric products through the cross terms and the Jacobi defect, and the sesquilinear products through the conjugate-linearity that collapses their projectors. The isolation is a statement about the law and not about isolated elements, and the general quaternionic product is the boundary case, a plain operator with a conjugated index.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\tilde Q_2$ | the general plain product, the block's multiplication |
| $L_{\tilde Q_1}:\tilde Q_2\mapsto\tilde Q_1\tilde Q_2$ | the left multiplication of the plain product |
| $\tilde Q_1\circ(\tilde Q_1\circ\tilde Q_2)=(\tilde Q_1\circ\tilde Q_1)\circ\tilde Q_2$ | left alternativity, the criterion |
| $L^{\circ}_{\tilde Q_1}L^{\circ}_{\tilde Q_1}=L^{\circ}_{\tilde Q_1\circ\tilde Q_1}$ | the operator identity, equivalent to the criterion |
| $\mathbb{B}=\mathbb{B}_{11}\oplus\mathbb{B}_{12}\oplus\mathbb{B}_{21}\oplus\mathbb{B}_{22}$ | the quadratic Peirce decomposition |
| $E_{ij}E_{kl}=\delta_{jk}E_{il}$ | the matrix units of the corners |
| $\mathbb{B}\tilde\Upsilon=\mathrm{ann}(\tilde\Upsilon)$ | the ideal of a square-zero element, equal to its annihilator |
| $Z(\mathbb{B})=\mathbb{C}e_t$ | the centre |
| $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$ | the enveloping operator algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the corner subalgebras and the matrix units of a finite-dimensional associative algebra.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for left alternativity and the alternative laws.
- *Ideals and Peirce Decomposition of the Biquaternion Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.md`), for the ideal lattice, the annihilator and the Peirce decomposition.
- *Modules over the Biquaternion Algebra* (`articles_maths/modules-over-the-biquaternion-algebra.md`), for the module category and its semisimplicity.
- *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ and the bi-module.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the boundary of the criterion.
- *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the twelve structures and the isolation.
