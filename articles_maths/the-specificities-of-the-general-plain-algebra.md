# __The Specificities of the General Plain Algebra__

## Introduction

Of the twelve algebraic structures that the complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one makes it an associative unital algebra over $\mathbb{C}$: the **general plain bilinear product** $\tilde P\tilde Q$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the multiplication of *Introduction to the General Plain Algebra of Biquaternions*. Every unital result of this block belongs to it alone — the ideal lattice and the Peirce decomposition of *Ideals and Peirce Decomposition of the General Plain Algebra*, the module theory of *Modules over the General Plain Algebra of Biquaternions*, the corner subalgebras and the enveloping algebra of *The Enveloping Algebra of the General Plain Algebra and the Bi-module Structure* — and this article states the exact reason, in one identity, and then separates the properties that are exclusive from the properties that only look exclusive.

The reason is not associativity as such but a weaker law. The sentence "an idempotent gives a projector" is a statement about the operator $L_{\tilde\Pi}:\tilde Y\mapsto\tilde\Pi\circ\tilde Y$, and the statement that the operator of a square is the square of the operator, $L_{\tilde X}\circ L_{\tilde X}=L_{\tilde X\circ\tilde X}$, holds for every element exactly when the product is **left-alternative**. Among the twelve that is the general plain product and no other. The eleven are built from it by twisting a slot with a conjugation or by (anti)symmetrising, and each of those three operations destroys the law, so the failure is not the accident of one witness but a structural consequence of how the twelve are made.

The consequence is the point of the article. Only in the general plain algebra are the operator calculus of the idempotents, the square-zero calculus of the nilpotents, the flag of the one-sided ideals and the Peirce decomposition available as **theorems**. Elsewhere single elements do behave well — the unit gives a projector in the symmetric structures, the plain idempotents in the general quaternionic product — and no other structure carries the theory. The one genuine border case is the general quaternionic product, whose operators are plain ones with a conjugated index; it is *The Specificities of the General Quaternionic Algebra* and is stated here only as the boundary of the criterion.

**Placement.** The article is the fourth and closing entry of the *Specific Theory* section of the general plain algebra, after *Ideals and Peirce Decomposition of the General Plain Algebra*, *Modules over the General Plain Algebra of Biquaternions* and *The Enveloping Algebra of the General Plain Algebra and the Bi-module Structure*, whose results it reads back as consequences of one identity. It is a synthesis: it uses the classification of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the four products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the property table of *Comparison Between the Four General Products* and the closure failure of *Relations Between the Four General Products* §*The Left Multiplications*. It is the twin of *The Specificities of the General Quaternionic Algebra*, and the two are read together.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. The **plain product** is written as juxtaposition $\tilde P\tilde Q$; a product written $\circ$ is a generic one, and its identity is stated at each use. The natural conjugation is ${}^{\natural}$, $\tilde Q^{\natural}=Q_0-\mathbf Q$; the star is ${}^{*}$, the Hermitian conjugation of the corpus, $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$, the composite of the natural conjugation with the conjugation of the coefficients; and the **bar** is $\overline{\tilde Q}=\tilde Q^{\natural*}=\tilde Q^{*\natural}$, the conjugation of the coefficients alone; all three fix $e_0$, and the star and the bar are conjugate-linear. The **left multiplication** of a product $\circ$ by $\tilde X$ is the map $L^{\circ}_{\tilde X}:\tilde Y\mapsto\tilde X\circ\tilde Y$, and the superscript is dropped for the plain product. The subscript is the element, never the operator: $L_{\tilde P}L_{\tilde R}$ is the composite $L_{\tilde P}\circ L_{\tilde R}$. An **idempotent** of the algebra is an element equal to its own square, and a **projector** is an idempotent operator, that is an idempotent of the morphism space; the zero operator is one, and the two levels are never interchanged. An idempotent element corresponds to a projector when its multiplication operator is idempotent, and the content of the criterion below is exactly that correspondence for the plain product.

## The Criterion

**Definition (left alternativity).** A product $\circ$ on the complex space is **left-alternative** when

$$
\tilde X\circ(\tilde X\circ\tilde Y)=(\tilde X\circ\tilde X)\circ\tilde Y\qquad\text{for all }\tilde X,\tilde Y .
$$

**Theorem (the criterion).** For a product $\circ$ the operator identity

$$
L^{\circ}_{\tilde X}\circ L^{\circ}_{\tilde X}=L^{\circ}_{\tilde X\circ\tilde X}\qquad\text{for every }\tilde X
$$

holds exactly when $\circ$ is left-alternative.

**Proof.** Evaluate both sides at $\tilde Y$: the left side is $\tilde X\circ(\tilde X\circ\tilde Y)$ and the right side is $(\tilde X\circ\tilde X)\circ\tilde Y$. The two operators agree for all $\tilde X,\tilde Y$ exactly when the two elements agree for all $\tilde X,\tilde Y$, which is the definition of left alternativity.

**Corollary (idempotents and nilpotents).** In a left-alternative structure every idempotent gives a **projector**, $L_{\tilde\Pi}^{2}=L_{\tilde\Pi}$, and every square-zero element gives a **square-zero operator**, $L_{\tilde\Upsilon}^{2}=0$.

**Proof.** By the theorem $L_{\tilde\Pi}^{2}=L_{\tilde\Pi\circ\tilde\Pi}=L_{\tilde\Pi}$ and $L_{\tilde\Upsilon}^{2}=L_{\tilde\Upsilon\circ\tilde\Upsilon}=L_{0}=0$.

The corollary is the whole mechanism by which an element produces subspaces, and the reason is worth stating. A projector has an image and a kernel, the two are subspaces, they add to the whole space, and the image is the fixed set; an element of square zero gives an operator whose image lies in its kernel, so it produces a **flag** $\{0\}\subseteq\mathrm{im}\,L\subseteq\ker L\subseteq\mathbb{B}$. Neither construction has any reason to exist without the identity of the theorem.

**Remark (one-sided by construction).** The criterion uses the left multiplications, and the mirror statement with the right multiplications characterizes right alternativity; a product is associative exactly when the two laws of the criterion hold together. Left alternativity is strictly weaker than associativity — the octonions are left-alternative and not associative — so the corollary is not associativity in disguise, and the criterion is the sharp threshold of the theories that follow.

## The Eleven Failures

The twelve structures are generated from the plain product by three independent operations, and this is why the plain one stands alone.

**Theorem (the plain product is the only left-alternative one).** Of the twelve structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the general plain bilinear product is the only left-alternative one.

**Proof.** The four general products are $\tilde X\circ\tilde Y=\theta(\tilde X)\phi(\tilde Y)$ with $\theta$ the identity or the natural conjugation ${}^{\natural}$ and $\phi$ the identity or the star ${}^{*}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), and the three operations of each family are the product, its symmetrisation and its antisymmetrisation. The plain product is the case $\theta=\phi=\mathrm{id}$, and it is left-alternative because it is associative. Each of the three operations destroys the law: the twisting of the first slot at §*The Twisted First Slot*, the twisting of the second slot at §*The Twisted Second Slot*, and the symmetrisation and the antisymmetrisation at §*The Symmetrisation and the Antisymmetrisation*. Each of the eleven remaining structures is obtained from the plain product by at least one of the three, since the twelve are the four twist combinations taken with the product, the symmetrisation and the antisymmetrisation, and the plain product is the combination with no twist and no symmetrisation.

### The Twisted First Slot

**Proposition (the general quaternionic product is not left-alternative).** For the product $\tilde X\circ\tilde Y=\tilde X^{\natural}\tilde Y$ the law fails, and the failure is visible on the units,

$$
e_1\circ(e_1\circ e_0)=-e_0,\qquad (e_1\circ e_1)\circ e_0=e_0 .
$$

**Proof.** $e_1\circ e_0=e_1^{\natural}e_0=-e_1$, so the left side is $e_1\circ(-e_1)=e_1^{\natural}(-e_1)=e_1^{2}=-e_0$; and $e_1\circ e_1=e_1^{\natural}e_1=-e_1^{2}=e_0$, so the right side is $e_0\circ e_0=e_0^{\natural}e_0=e_0$.

**Remark (why the first slot is the wrong one).** The two sides are $x^{\natural}(x^{\natural}y)$ and $(x^{\natural}x)^{\natural}y=x^{\natural}x^{\natural}y$, the second step using that ${}^{\natural}$ is an anti-automorphism of order two. The law would therefore require $x^{\natural}x^{\natural}=x^{\natural}x$ for every $x$, and at $x=e_1$ the left side is $-e_0$ and the right side $e_0$. The twist is by an **anti**-automorphism, and an anti-automorphism placed in the first slot is carried by the associativity of the plain product to the far side of the product, where it reverses the order of the two factors; the plain product tolerates that twist on the operator side and not on the element side, which is the subject of the companion article.

### The Twisted Second Slot

**Proposition (the parity obstruction).** Let the product be conjugate-linear in its second slot and nothing else, as it is for the general plain sesquilinear product, the general quaternionic sesquilinear product, the symmetric plain sesquilinear product and the symmetric quaternionic sesquilinear product. Then no nonzero element is a projector: if $L^{\circ}_{\tilde X}$ is a projector then $\tilde X=0$.

**Proof.** Such a product gives a conjugate-linear $L^{\circ}_{\tilde X}$, while the composite $L^{\circ}_{\tilde X}\circ L^{\circ}_{\tilde X}$ is linear. The projector identity makes the two the same map, which is therefore simultaneously $\mathbb{C}$-linear and conjugate-linear, hence zero; so $L^{\circ}_{\tilde X}=0$, and the operator vanishes only at the origin, each of the four products reading its argument through a non-degenerate pairing, so $\tilde X=0$.

The statement is stronger than the failure of left alternativity: the class of projectors collapses to the single operator $0$. The collapse is confined to the projectors and does not by itself empty the identity, which is a different condition. For the symmetric plain sesquilinear product the identity $L^{\circ}_{\tilde X}{}^{2}=L^{\circ}_{\tilde X\circ\tilde X}$ holds along the whole central line, both sides reading $\lambda^{2}\overline{Y_0}e_0$ at $\tilde X=\lambda e_0$, so there the identity is met by elements whose left multiplication is conjugate-linear and hence not a projector. An identity satisfied at one element is the phenomenon of §*The Boundary of the Criterion*, and it is not the collapse of the projector class. The witness of the failure of left alternativity is the general plain sesquilinear product at the unit,

$$
e_1\circ(e_1\circ e_1)=e_1,\qquad (e_1\circ e_1)\circ e_1=-e_1 ,
$$

computed from $e_1\circ e_1=e_1e_1^{*}=e_0$. The related failure of closure of the left multiplications, that the composite of two of them is linear and no longer sesquilinear, is *Relations Between the Four General Products* §*The Left Multiplications*, and it is a different statement: the closure failure is about the family of operators, the parity obstruction about their fixed points.

### The Symmetrisation and the Antisymmetrisation

**Proposition (the symmetric and the antisymmetric products are not left-alternative).** For the symmetric plain product $\tilde X\circ\tilde Y=\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ and the antisymmetric plain product $\tilde X\circ\tilde Y=\tfrac12(\tilde X\tilde Y-\tilde Y\tilde X)$ the law fails,

$$
e_1\circ(e_1\circ e_2)=0\neq-e_2=(e_1\circ e_1)\circ e_2,\qquad
e_1\circ(e_1\circ e_2)=-e_2\neq0=(e_1\circ e_1)\circ e_2 .
$$

**Proof.** For the symmetric product $e_1\circ e_1=e_1^{2}=-e_0$ and $e_1\circ e_2=\tfrac12(e_1e_2+e_2e_1)=\tfrac12(e_3-e_3)=0$, so the left side of the first display is $e_1\circ 0=0$ while the right side is $(-e_0)\circ e_2=-\tfrac12(e_2+e_2)=-e_2$. The antisymmetric mirror has $e_1\circ e_1=0$ and $e_1\circ e_2=\tfrac12(e_3+e_3)=e_3$, so the left side of the second display is $e_1\circ e_3=\tfrac12(e_1e_3-e_3e_1)=\tfrac12(-e_2-e_2)=-e_2$ while the right side is $0\circ e_2=0$.

**Remark (why the symmetrisation fails).** For the symmetric product the left multiplication is $L^{\circ}_{\tilde X}=\tfrac12(L_{\tilde X}+R_{\tilde X})$, half the sum of a plain left and a plain right multiplication, and its square contains the cross terms $L_{\tilde X}R_{\tilde X}$ and $R_{\tilde X}L_{\tilde X}$ beside the two pure squares; the cross terms do not recombine into a single multiplication by an element, so the composite is no longer of the form $L^{\circ}_{\tilde Z}$. The point is exactly the failure of commutativity to control associativity: a commutative left-alternative algebra is associative, and the symmetric products are commutative without being associative.

**Remark (why the antisymmetrisation fails).** For the antisymmetric product $\tilde X\circ\tilde X=0$ for every $\tilde X$, so left alternativity would read $\tilde X\circ(\tilde X\circ\tilde Y)=0$ for every $\tilde X,\tilde Y$, that is $L^{\circ}_{\tilde X}{}^{2}=0$ for every $\tilde X$. A Lie algebra in which every adjoint map is square-zero is two-step nilpotent; the antisymmetrisations of the twelve are the cross product on the vector part and its quaternionic and sesquilinear variants, whose nonzero adjoint maps are regular nilpotents rather than square-zero. The two antisymmetric sesquilinear products are the antisymmetrisations of two of the four products with a purely conjugate-linear second slot, so their projectors collapse as well, and this time not by parity but by the antisymmetrisation.

**Remark (index three).** The antisymmetric family has a further feature that no other family shares. For the antisymmetric plain product and the antisymmetric quaternionic product the operator of the isotropic pure element $e_1+ie_2$ has index three, $L^{2}\neq0$ and $L^{3}=0$, because the product is the cross product on the vector part and the adjoint map of an isotropic element of the three-dimensional simple Lie algebra is a regular nilpotent; the two-step flag, which is the operator shape of a square-zero element, is a shape that family does not produce. In the antisymmetric plain product the centre is the left annihilator, so the zero operator occurs there; in the antisymmetric quaternionic product the unit gives instead the projection onto the vector subspace.

### The Verdicts

The twelve structures are compared below. The second column is the criterion, and the third column names, structure by structure, the notable elements whose left multiplication is a projector; the zero element gives the zero operator in all twelve and is listed only where it is the whole answer.

| structure | left-alternative | what carries a projector |
|---|---|---|
| GPA | yes | every idempotent, whose projectors give the Peirce calculus |
| GQA | no | the plain idempotents, indexed by the plain product |
| SPA | no | the unit alone, whose operator is the identity |
| SQA | no | the elements of scalar coordinate $1$, whose operator is a rank-one projection onto the central line |
| APA | no | none, the centre giving the zero operator |
| AQA | no | the unit, whose operator is the projection onto the vector subspace |
| GPS, GQS | no | none, the zero operator alone |
| SPS, SQS | no | none, the zero operator alone |
| APS, AQS | no | none, the zero operator alone |

The table records theorems, not coincidences, and the two are kept apart. Single elements of the other structures do give square-zero operators without being square-zero elements — in the symmetric quaternionic and the symmetric plain sesquilinear products the basis vectors $e_k$ satisfy $L_{e_k}^{2}=0$ — and none of those examples carries a decomposition, because a decomposition needs the identity of §*The Criterion* and not a case of it.

## What the Criterion Delivers

Only for the plain product does the corollary of §*The Criterion* hold as a theorem, and the whole unital theory of the block is its consequence. The list is the table of contents of the section this article closes.

- **Projectors and their spaces.** For an idempotent $\tilde\Pi$ the operator $L_{\tilde\Pi}$ is a projector, its image $\tilde\Pi\mathbb{B}$ and its kernel $(e_0-\tilde\Pi)\mathbb{B}$ are $\mathbb{C}$-subspaces, and $\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}$; the two summands are the minimal left ideals of *Ideals and Peirce Decomposition of the General Plain Algebra*.
- **The Peirce decomposition.** Relative to a pair of orthogonal idempotents the algebra splits into the four corners, the diagonal corners $e\mathbb{B}e$ and $f\mathbb{B}f$ are subalgebras with units $e$ and $f$, and the mixed spaces $e\mathbb{B}f$ and $f\mathbb{B}e$ are bimodules over the two corners with identically zero product, $(e\mathbb{B}f)(e\mathbb{B}f)=0$, so that they carry no unit and no algebra structure of their own. The construction uses associativity twice, in reading the two maps as projectors and in adding their images, and it is the part of the theory no other structure supports; it is also a construction of the **plain** product, and §*The Peirce Elements in the Twelve Structures* shows how differently the four general products read the same four elements.
- **The ideals and the flag.** The left and the right ideals, the minimal ones, the classification $0$, the minimal ideals, $\mathbb{B}$, and the coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the ideal generated by a nilpotent with its annihilator.
- **The modules.** The regular module and its category, the projective objects, the Morita equivalence with the complex vector spaces, all of *Modules over the General Plain Algebra of Biquaternions*.

**Remark (the universal residue).** What survives in all twelve structures, and is therefore a specificity of none of them, is the one-dimensional span of a nonzero idempotent, a subalgebra wherever the idempotent exists, and the one-dimensional span of a nonzero square-zero element, a subalgebra with vanishing product; both are true by definition, $\tilde\Pi\circ\tilde\Pi=\tilde\Pi$ and $\tilde\Upsilon\circ\tilde\Upsilon=0$, and neither produces a decomposition of the ambient space.

## The Peirce Elements in the Twelve Structures

The criterion is also the reason the Peirce decomposition is a statement about the plain product and not about the space. The four elements that carry it — the idempotents $\tilde\Pi_1,\tilde\Pi_2$ and the square-zero elements $\tilde\Upsilon_1,\tilde\Upsilon_2$ of *Idempotents of the General Plain Algebra* and *Ideals and Peirce Decomposition of the General Plain Algebra* — are read differently by the twelve structures, and the readings are computed from their coordinates.

**The standard elements in the four general products.** With the products $\tilde X\circ\tilde Y=\theta(\tilde X)\phi(\tilde Y)$, $\theta$ the identity or the natural conjugation ${}^{\natural}$ and $\phi$ the identity or the star ${}^{*}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), the squares of the standard elements are

| product | $\tilde\Pi_1\circ\tilde\Pi_1$ | $\tilde\Upsilon_1\circ\tilde\Upsilon_1$ |
|---|---|---|
| plain $\tilde X\tilde Y$ | $\tilde\Pi_1$ | $0$ |
| general quaternionic $\tilde X^{\natural}\tilde Y$ | $0$ | $0$ |
| general plain sesquilinear $\tilde X\tilde Y^{*}$ | $\tilde\Pi_1$ | $\tilde\Pi_1$ |
| general quaternionic sesquilinear $\tilde X^{\natural}\tilde Y^{*}$ | $0$ | $-\tilde\Pi_1$ |

with the mirror entries for $\tilde\Pi_2$ and $\tilde\Upsilon_2$, which are idempotent, square-zero, idempotent and square-zero respectively in the same four products, and whose sesquilinear squares are $\tilde\Upsilon_2\circ\tilde\Upsilon_2=\tilde\Pi_2$ and $-\tilde\Pi_2$. The pattern is by slot. The **first slot** decides idempotency: the plain first slot keeps $\tilde\Pi_1$ idempotent, and the natural first slot kills it, because the natural conjugation exchanges the two idempotents and $\tilde\Pi_1^{\natural}\tilde\Pi_1=\tilde\Pi_2\tilde\Pi_1=0$. The **second slot** decides the nilpotence: the plain second slot leaves $\tilde\Upsilon_1$ square-zero, and the star reads the second factor as $\tilde\Upsilon_1^{*}=\tilde\Upsilon_2$, so that the square of the nilpotent is the idempotent, $\tilde\Upsilon_1\circ\tilde\Upsilon_1=\tilde\Upsilon_1\tilde\Upsilon_2=\tilde\Pi_1$, with the sign reversed in the quaternionic sesquilinear product. The second-slot twist by the star does not disturb the idempotents, $\tilde\Pi_i^{*}=\tilde\Pi_i$, and it is the same star that pairs the two nilpotents in *Conventions in Mathematics*, §*The nilpotent convention*.

**Where the idempotents survive, the corollary fails.** In the general plain sesquilinear product $\tilde\Pi_1$ is idempotent, so the corollary of §*The Criterion* would give the projector $L^{\circ}_{\tilde\Pi_1}$; the product is not left-alternative, so it does not, and the surviving idempotents produce no splitting of the space. The Peirce decomposition of *Ideals and Peirce Decomposition of the General Plain Algebra* — the four corners, the multiplication table $E_{ij}E_{kl}=\delta_{jk}E_{il}$ of the matrix units, the matrix model and the rigidity of the decomposition by two primitive idempotents — is therefore a decomposition of the **plain** product, and it does not transport to the other eleven structures.

**No idempotent survives the antisymmetrisation.** The four antisymmetrised structures have no idempotent but $0$: an antisymmetrised product satisfies $\tilde X\ominus\tilde X=0$ identically, so an idempotent obeys $\tilde\Pi=\tilde\Pi\ominus\tilde\Pi=0$. The four antisymmetric structures therefore admit no Peirce decomposition at all, there being no nonzero idempotent to decompose with and no projector to decompose by. Of the four symmetrised structures, each has the idempotents of its underlying product and no others, since $\tilde\Pi\odot\tilde\Pi=\tilde\Pi\circ\tilde\Pi$; the idempotents and the Peirce decomposition live on the symmetric side of the twelve.

## The Boundary of the Criterion

Two statements are easily confused and are kept apart here.

1. **As an identity, left alternativity is exactly the threshold.** The identity $L_{\tilde X}^{2}=L_{\tilde X\circ\tilde X}$ for every $\tilde X$ is equivalent to left alternativity, and the plain product is the only one of the twelve that satisfies it.
2. **As a statement about one element, the identity can hold outside the plain product.** An operator $L_{\tilde X}$ may be a projector in a structure that is not left-alternative, because the identity is then demanded at one element and not at all of them. The structured case is the general quaternionic product, where the identity holds exactly at the elements whose natural conjugate is a plain idempotent; there the projectors form a four-real-parameter family, they are indexed by the idempotents of the plain product, and the algebra disowns them, its own idempotents being $0$ and $e_0$ alone. That reading, with the left-ideal lattice it produces, is *The Specificities of the General Quaternionic Algebra*. The symmetric quaternionic product is the second case, where the scalar coordinate decides everything and the elements of scalar coordinate $1$, a hyperplane, give pairwise distinct rank-one projections; it is *The Specificities of the Symmetric Quaternionic Algebra*.

**Remark (the sharp form of the specificity).** The correct exclusive statement is therefore not that no other structure has a projector, but that no other structure has the **theorem**: the general plain algebra is the only one in which every idempotent gives a projector and every square-zero element gives a square-zero operator. This is why the Peirce theory, the ideal lattice and the module theory are properties of the plain product and are not transferable, and it is the reason the twelve are not twelve copies of one theory but one theory with eleven deformations.

## Summary

The general plain bilinear product is the only one of the twelve structures of the complex space that is left-alternative, and left alternativity is the exact condition under which the operator of a square is the square of the operator. The criterion is the identity $L_{\tilde X}\circ L_{\tilde X}=L_{\tilde X\circ\tilde X}$ for every $\tilde X$, equivalent to $\tilde X\circ(\tilde X\circ\tilde Y)=(\tilde X\circ\tilde X)\circ\tilde Y$, and its corollary is that in a left-alternative structure the left multiplication of an idempotent is idempotent and a square-zero element gives a square-zero operator. The eleven other structures are built from the plain product by twisting a slot with a conjugation or by symmetrising, and each operation destroys the law: the first-slot twist by the anti-automorphism ${}^{\natural}$ fails at $e_1$, the second-slot twist by the star makes the left multiplications conjugate-linear and collapses the projectors to $0$, the symmetrisation produces the cross terms of a left and a right multiplication, and the antisymmetrisation would force a two-step nilpotent Lie algebra while the operators of that family have index three. The consequence is that the operator calculus, the Peirce decomposition, the ideal lattice, the flag of the nilpotents and the module theory belong to the plain product alone, and the correct exclusive statement is about the theorem and not about isolated elements: the plain algebra is the only structure in which every idempotent gives a projector, and the general quaternionic and symmetric quaternionic products are the two border cases, where projectors exist in families indexed by the elements of other products. The Peirce elements themselves are read differently by the four general products — the first slot deciding idempotency and the second the square of the nilpotent — and the four antisymmetrised structures have no idempotent but the zero element, so that the corners, the matrix units and the rigidity of *Ideals and Peirce Decomposition of the General Plain Algebra* are properties of the plain product alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\circ$ | a generic product, specified at each use |
| $L^{\circ}_{\tilde X}$ | the left multiplication $\tilde Y\mapsto\tilde X\circ\tilde Y$ |
| $L_{\tilde X}$, $R_{\tilde X}$ | the left and the right multiplication of the plain product |
| $\natural$, $*$, $\overline{\cdot}$ | the natural, the Hermitian (star) and the coefficient (bar) conjugations, all fixing $e_0$ |
| $\tilde\Pi$, $\tilde\Upsilon$ | an idempotent, a square-zero element |
| $\mathbb{B}$ | the complex space $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| GPA … AQS | the twelve structures, coded as in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and the right multiplications of a non-associative algebra and the alternative laws.
- K. A. Zhevlakov, A. M. Slin'ko, I. P. Shestakov and A. I. Shirshov, *Rings That Are Nearly Associative* (Academic Press, 1982), for the algebra of the alternative, Jordan and Lie laws and the identities that separate them.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the corner subalgebras and the ideal lattice of the associative theory.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the structure that recovers projectors and left ideals with a different indexing.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the second border case, where the projectors are a hyperplane of rank-one projections.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table against which the criterion is read.
