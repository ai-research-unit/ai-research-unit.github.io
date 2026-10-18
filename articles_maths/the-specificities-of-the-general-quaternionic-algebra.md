# __The Specificities of the General Quaternionic Algebra__

## Introduction

The general quaternionic bilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ is the second of the four general products of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, and as an element-theoretic object it is poor. It has a left unit and no right one, no centre at all, and it is neither associative nor alternative nor flexible nor power associative; what it is and what it is not is stated in *Introduction to the General Quaternionic Algebra*, and its element classes — the idempotents, the nilpotents, the zero divisors — are the subject of *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, *Zero Divisors of the General Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*. As an **operator-theoretic** object it is the opposite: almost everything survives, in a one-sided form.

The reason is a single identity. The natural conjugation is an anti-automorphism, so the product is the isotope of the plain product determined by the pair $(\natural,\mathrm{id})$, and the twist sits in the **first** slot, which is the slot a left multiplication reads. Hence

$$
L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1^{\natural}\tilde Q_2 ,
$$

the left multiplication of the quaternionic product by $\tilde Q_1$ is the **plain** left multiplication by the conjugated element. Every operator statement about the quaternionic product is therefore an element statement about the plain product, and the whole associative theory becomes available on the operator side. The price is that the index is shifted: the operators of the algebra are plain, and the elements they are indexed by are conjugated, so the element classes that produce decompositions are *not* the element classes of the algebra.

This article collects the consequences. The projector criterion becomes "(the conjugate of) a plain idempotent", the left ideals of the quaternionic product are exactly the left ideals of the plain product, the square-zero operators come from the pure isotropic cone, and the two classes are strictly smaller than the nilpotent cone of the algebra. The paradoxical corollary is that the plain idempotents are $\star$-**nilpotents** whose left multiplication is a **projector**, so the quaternionic product realises a projector on an element of vanishing square, a combination the plain product forbids. The twinned article is *The Specificities of the Biquaternion Algebra*, which states why the plain product alone carries the theory as a theorem.

**Placement.** The article is the fifth entry, and the synthesis, of the *Specific Theory* section of the general quaternionic algebra, after *The Associator and the Ternary Product of the Quaternionic Product*, *The Symmetrised Quaternionic Product and the Hermitian Subspace*, *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Quaternionic Product on the Quaternion Subspace*. It uses the isotope reading of *Introduction to the General Quaternionic Algebra*, the monoid law of *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, the idempotents of *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, the norm and the one-sided equations of *Norm and Invertibility in the General Quaternionic Algebra*, the zero divisors and their annihilators of *Zero Divisors of the General Quaternionic Algebra*, the nilpotent cone of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, the plain element classes of *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*, and the plain left ideals of *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y=\vec e_z$ and central scalar imaginary $i$. Juxtaposition is the **plain** product $\tilde Q_1\tilde Q_2$ and $\star$ is the **quaternionic product** $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$; the subscript of an operator is the element it is indexed by, so $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\star\tilde Q_2$ and $L_{\tilde Q_1}L_{\tilde Q_4}$ is the composite. The natural conjugation is ${}^{\natural}$, $\tilde Q_2^{\natural}=Q_{2t}-\vec Q_2$, the coefficientwise conjugation is $\overline{\cdot}$, and the star is their composite ${}^{*}=\overline{\cdot}\circ{}^{\natural}$; all three fix $e_t$. The **norm** is the central square $\langle\tilde Q\rangle_{\natural}e_t=\tilde Q\tilde Q^{\natural}$ with $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, and its vanishing set is the zero-divisor cone (*Norm and Invertibility in the General Quaternionic Algebra*, *Zero Divisors of the General Quaternionic Algebra*). An element is **pure** when its scalar part vanishes, and **isotropic** when its vector part satisfies $(\vec Q_1,\vec Q_1)=0$ for the complex bilinear form $(\vec Q_1,\vec Q_2)=\sum_k Q_{1,k}Q_{2,k}$. An **idempotent** of the algebra is an element equal to its own square, and a **projector** is an idempotent operator, that is an idempotent of the morphism space; the zero operator is one, and the two levels are never interchanged. An idempotent element corresponds to a projector when its multiplication operator is idempotent, and the content of §*The Projectors* is exactly that correspondence, with the index conjugated.

## The Isotope Identity

**Proposition (the left multiplications are plain ones).** For every $\tilde Q_1$,

$$
L_{\tilde Q_1}=L^{\mathrm{plain}}_{\tilde Q_1^{\natural}},\qquad
L_{\tilde Q_1}L_{\tilde Q_4}=L_{\tilde Q_4\tilde Q_1} .
$$

**Proof.** The first display is the definition of $\star$ read as an operator identity, $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1^{\natural}\tilde Q_2$. For the second, $L_{\tilde Q_1}L_{\tilde Q_4}(\tilde Q_2)=\tilde Q_1^{\natural}(\tilde Q_4^{\natural}\tilde Q_2)=(\tilde Q_1^{\natural}\tilde Q_4^{\natural})\tilde Q_2$, and $\tilde Q_1^{\natural}\tilde Q_4^{\natural}=(\tilde Q_4\tilde Q_1)^{\natural}$ because ${}^{\natural}$ is an anti-automorphism, so the composite is $L_{\tilde Q_4\tilde Q_1}(\tilde Q_2)$.

The composition law is the reversed one, and it is stated with the monoid it defines in *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, where it is also proved that the family of left multiplications is a monoid isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$, and that the two sesquilinear products fail even that. What the present article adds is the reading of the first display as an **element dictionary**: every operator of $\star$ is an operator of the plain product, applied to a conjugated element.

**Corollary (linearity and the unit).** The operators $L_{\tilde Q_1}$ are $\mathbb{C}$-linear and faithful in $\tilde Q_1$; $e_t$ is a left unit of $\star$ and there is no right one, the right action being the conjugation $\tilde Q_2\star e_t=\tilde Q_2^{\natural}$, and the centre of $\star$ is trivial (*Introduction to the General Quaternionic Algebra*).

**Proof.** $L^{\mathrm{plain}}$ is $\mathbb{C}$-linear, and it is faithful because $L^{\mathrm{plain}}_{\tilde Q_2}=0$ forces $\tilde Q_2=L^{\mathrm{plain}}_{\tilde Q_2}(e_t)=0$. The unit statements are the displays $e_t\star\tilde Q=\tilde Q$ and $\tilde Q\star e_t=\tilde Q^{\natural}$, and the triviality of the centre is the companion article's proposition.

The faithfulness is what makes the dictionary invertible: an operator identity of $\star$ is an element identity of the plain product, with no loss. It is used at every step below.

## The Projectors

**Theorem (the projector criterion).** The operator $L_{\tilde Q_1}$ is a projector if and only if $\tilde Q_1^{\natural}$ is an idempotent of the plain product.

**Proof.** By §*The Isotope Identity* $L_{\tilde Q_1}^{2}=L^{\mathrm{plain}}_{\tilde Q_1^{\natural}}{}^{2}=L^{\mathrm{plain}}_{(\tilde Q_1^{\natural})^{2}}$, and $L_{\tilde Q_1}=L^{\mathrm{plain}}_{\tilde Q_1^{\natural}}$. By the faithfulness the two are equal exactly when $(\tilde Q_1^{\natural})^{2}=\tilde Q_1^{\natural}$, which is the stated condition.

**Corollary (the family of projectors).** The elements whose left multiplication is a projector are exactly the plain idempotents. Their number is two trivial ones, $0$ and $e_t$, and a family of complex dimension two; the element $\tilde\Pi$ gives a projector for $\star$ exactly when $\tilde\Pi^{2}=\tilde\Pi$ for the plain product.

**Proof.** The natural conjugation is an involution of the algebra, so it permutes the plain idempotents and $\tilde Q_1^{\natural}$ is a plain idempotent exactly when $\tilde Q_1$ is one. The count of the plain idempotents is *Idempotents of the General Plain Algebra*: beside $0$ and $e_t$, the idempotents are $\tfrac12(e_t+\tilde\Xi)$ with $\tilde\Xi$ pure and $\tilde\Xi^{2}=e_t$, a quadric in the three complex coordinates of the vector part, of complex dimension two.

**Remark (the algebra disowns them).** The idempotents of $\star$ are $0$ and $e_t$ alone. Indeed $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ is central for every $\tilde Q$, so an idempotent of $\star$ is central, hence a complex multiple of $e_t$, hence $0$ or $e_t$; the statement is the theorem of *Square Roots of One and the Idempotents of the General Quaternionic Algebra*. The projectors of §*The Projectors*, by contrast, come in a family of complex dimension two, and all but two of them are indexed by elements that are **not** idempotents of $\star$. This is the first specificity of the algebra: it has a full family of projectors, and its own idempotent equation recognizes almost none of them.

**Corollary (a projector on a square-zero element).** Every nontrivial plain idempotent $\tilde\Pi$ is a **nilpotent** of $\star$, and its $\star$-left multiplication is a projector,

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi^{\natural}\tilde\Pi=\langle\tilde\Pi\rangle_{\natural}e_t=0,\qquad L_{\tilde\Pi}^{2}=L_{\tilde\Pi}\neq0 .
$$

**Proof.** The middle equality is the central-square identity of the plain product, and $\langle\tilde\Pi\rangle_{\natural}=0$ for a nontrivial idempotent because $\tilde\Pi\tilde\Pi^{\natural}=0$ makes it a zero divisor of the non-pure family (*Zero Divisors of the Biquaternion Algebra*); the first equality is the definition of $\star$, and the operator statement is the theorem of §*The Projectors*. The two displays are compatible because they concern different objects: the *element* is square-zero, the *operator* is a projector.

The corollary is worth pausing on. In the plain algebra an idempotent and a nilpotent are disjoint, meeting only at the origin (*Nilpotents of the General Plain Algebra*), so no element both vanishes when squared and has an idempotent left multiplication. The quaternionic product separates the two properties and assigns them to different levels: the element $\tilde\Pi$ has vanishing square, and the operator it defines is a projector with a two-dimensional image. The decomposition below therefore survives on an element of the nilpotent cone.

## The Orthogonal Pairs and the Decomposition

**Proposition (orthogonal projectors).** Let $\tilde\Pi_1$ be a nontrivial plain idempotent and let $\tilde\Pi_2=e_t-\tilde\Pi_1$. Then

$$
L_{\tilde\Pi_1}+L_{\tilde\Pi_2}=\mathrm{Id},\qquad L_{\tilde\Pi_1}L_{\tilde\Pi_2}=0,\qquad
\mathbb{B}=\tilde\Pi_1\star\mathbb{B}\oplus\tilde\Pi_2\star\mathbb{B},
$$

and each summand is a minimal left ideal of the plain algebra of complex dimension two.

**Proof.** The operators are plain left multiplications by $\tilde\Pi_1^{\natural}$ and $\tilde\Pi_2^{\natural}$ by §*The Isotope Identity*, and $L^{\mathrm{plain}}$ is additive and multiplicative, so $L_{\tilde\Pi_1}+L_{\tilde\Pi_2}=L^{\mathrm{plain}}_{e_t}=\mathrm{Id}$ and $L_{\tilde\Pi_1}L_{\tilde\Pi_2}=L^{\mathrm{plain}}_{\tilde\Pi_1^{\natural}\tilde\Pi_2^{\natural}}$. The two idempotents are orthogonal and their sum is $e_t$, so $\tilde\Pi_1^{\natural}\tilde\Pi_2^{\natural}=0$ and the images are complementary; being the minimal left ideals of *Ideals and Peirce Decomposition of the Biquaternion Algebra* they have complex dimension two.

**Remark (a real form from an involution, not from an idempotent).** In the sesquilinear structures the left multiplication of the unit is conjugate-linear and is not a projector; for the general plain, the general quaternionic and the symmetric quaternionic sesquilinear products it is an involution, $L_{e_t}^{2}=\mathrm{Id}$, and it splits the space into its fixed and its minus-one eigenspaces with no idempotent at all. The pair of the proposition is of the other kind: two genuine projectors, each of complex rank two, indexed by $\star$-nilpotents. The involution and the projector are the two mechanisms of the block and they are kept apart: an involution splits the space by its eigenvalues $\pm1$ and needs no idempotent, while a projector splits it by its image and kernel, and only the projector needs the criterion.

## The Left Ideals

**Theorem (the left ideals coincide with the plain ones).** A subspace $I$ of $\mathbb{B}$ is a left ideal of the quaternionic product if and only if it is a left ideal of the plain product. In particular the minimal left ideals of $\star$ are the minimal left ideals of the plain product, each of complex dimension two, and the lattice of left ideals is $0$, the minimal ideals, $\mathbb{B}$.

**Proof.** $I$ is a left ideal of $\star$ exactly when $\mathbb{B}\star I\subseteq I$, that is exactly when $\mathbb{B}^{\natural}I\subseteq I$; and $\mathbb{B}^{\natural}=\mathbb{B}$ because the natural conjugation is a bijection of the algebra onto itself, so the condition is $\mathbb{B}I\subseteq I$, the definition of a left ideal of the plain product. The minimal ones have complex dimension two by *Ideals and Peirce Decomposition of the Biquaternion Algebra*, and the lattice has the three levels stated because the plain algebra is simple of length two.

**Remark (what does not coincide).** The identification is one-sided and it stops at the modules. The **right** ideals are not the same: the right ideal generated by $\tilde Q_2$ under $\star$ is $\tilde Q_2^{\natural}\mathbb{B}$, the conjugate of a plain left ideal, and the right action is twisted by the conjugation as the corollary of §*The Isotope Identity* shows. The **two-sided** theory does not exist for $\star$, since the product has no right unit and no centre and is not associative, so the subalgebra statement, the corner subalgebras and the bimodule statements of the Peirce decomposition have no analogue and are not claimed.

**Remark (the corner has no meaning).** The Peirce corner is a construction of the associative theory, and this product shows why it is one. The two bracketings of the three factors give different spaces,

$$
(\tilde\Pi\star\mathbb{B})\star\tilde\Pi=\mathbb{B}\tilde\Pi,\qquad
\tilde\Pi\star(\mathbb{B}\star\tilde\Pi)=\tilde\Pi^{\natural}\mathbb{B}\tilde\Pi ,
$$

of complex dimension two and one respectively. The first is the plain right ideal generated by $\tilde\Pi$, because $(\tilde\Pi\star\tilde Q_2)\star\tilde\Pi=(\tilde\Pi^{\natural}\tilde Q_2)^{\natural}\tilde\Pi=\tilde Q_2^{\natural}\tilde\Pi\tilde\Pi=\tilde Q_2^{\natural}\tilde\Pi$; the second is the plain off-diagonal Peirce space of the two idempotents $\tilde\Pi^{\natural}$ and $\tilde\Pi$, because $\tilde\Pi\star\tilde Q_3=\tilde\Pi^{\natural}\tilde Q_3$. The failure of associativity is exactly what makes the two differ, so the third factor cannot be moved and the corner is not defined. This is the clearest sign that the subspaces of this algebra belong to a left-module theory and not to a subalgebra theory.

## The Square-Zero Operators

**Theorem (the square-zero criterion).** The operator $L_{\tilde Q}$ is square-zero if and only if $\tilde Q^{\natural}$ is a nilpotent of the plain product, that is if and only if $\tilde Q$ is pure and isotropic.

**Proof.** $L_{\tilde Q}^{2}=L^{\mathrm{plain}}_{(\tilde Q^{\natural})^{2}}$ by §*The Isotope Identity*, and the plain left multiplications are faithful, so $L_{\tilde Q}^{2}=0$ exactly when $(\tilde Q^{\natural})^{2}=0$: exactly when $\tilde Q^{\natural}$ is a plain nilpotent. The plain nilpotents are the pure isotropic elements (*Nilpotents of the General Plain Algebra*), and the natural conjugation fixes the scalar part and negates the vector part, so purity is preserved in both directions and $(\tilde\Xi,\tilde\Xi)$ is invariant; hence $\tilde Q^{\natural}$ is pure isotropic exactly when $\tilde Q$ is.

**Remark (the nilpotent cone is bigger than the square-zero set).** The nilpotents of $\star$ are the elements of vanishing central square, $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$, that is the whole zero-divisor cone, a complex cone of complex dimension three; the square-zero operators exist only on its pure part, the isotropic cone of complex dimension two. The gap is not empty: a complex multiple $\lambda\tilde\Pi$ with $\lambda\neq0$ of a nontrivial idempotent has $\langle\lambda\tilde\Pi\rangle_{\natural}=\lambda^{2}\langle\tilde\Pi\rangle_{\natural}=0$, so it is a nilpotent of $\star$, and at $\lambda=1$ its operator is a projector rather than a square-zero operator, while at $\lambda\neq1$ it is neither. This is the second specificity of the algebra: the nilpotent cone is product-defined and does not match the set of elements whose operator vanishes twice.

## The Isolation among the Twelve

The criterion of this article is the projector criterion, and it says that in the general quaternionic product an element gives a projector — and hence, with its complement, a decomposition — exactly when it is an idempotent of the **plain** product.

**Theorem (the criterion checked against the twelve).** Of the twelve structures, the general quaternionic product is the only one in which a family of projectors exists, is indexed by the idempotents of a product, and is **disowned** by the idempotents of the structure itself; the general plain product is the only one in which the projectors are indexed by its own idempotents; in the remaining ten structures a projector is an isolated accident — the zero operator, the unit, or the rank-one projections over a hyperplane — and never an element-to-operator correspondence carrying a decomposition.

*Proof.* The general quaternionic case is §*The Projectors* above: the criterion holds with the index conjugated, the indices are the plain idempotents, the product's own idempotents are $0$ and $e_t$, and the correspondence carries the decomposition of §*The Orthogonal Pairs and the Decomposition*. The general plain case is the criterion of *The Specificities of the Biquaternion Algebra*, where the correspondence between idempotents and projectors is a theorem. For the remaining ten, the projector equation has only isolated solutions — the zero operator, the projectors of the unit, or the rank-one projections over a hyperplane — and none of them is a family indexed by idempotents; the object that supports the decomposition is the correspondence of the criterion and not an isolated solution of the projector equation.

| structure | what the projector criterion gives |
|---|---|
| GPA | the theorem: every idempotent gives a projector, and the Peirce calculus follows |
| GQA | the criterion: the projectors exist, are indexed by the plain idempotents, and the product disowns them |
| the ten remaining | isolated projectors, no indexed family and no decomposition |

The isolation makes the specificity exact. The quaternionic product is not the plain product with one property removed; it is the structure in which the operator theory of the plain product survives entirely and the element theory of the plain product is carried by the wrong elements. The two halves of the block — the element classes of *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, *Zero Divisors of the General Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, and the operator theory of this article and of *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* — are the two readings of that one sentence.

## What the Algebra Is Not

The three losses are the reason the dictionary of §*The Isotope Identity* is one-sided, and they are stated together because they have one source, the absence of a two-sided unit and of a centre.

- **No right unit, no centre.** $\tilde Q\star e_t=\tilde Q^{\natural}$ is the conjugation and not the identity, and no element commutes with every element; so there is no two-sided object to build the subalgebra theory on, and the Peirce corner is not even well defined, its two bracketings differing as §*The Left Ideals* records.
- **No associativity, no alternativity, no flexibility, no power associativity at the element level.** The witnesses are in *Introduction to the General Quaternionic Algebra* and *The Associator and the Ternary Product of the Quaternionic Product*; the associator of $\star$ is the product of a fixed defect and the two factors, and no power of an element is well defined. The left-alternative law fails at $\tilde Q_1=\vec e_z$, $\tilde Q_2=-\vec e_z$, where $\tilde Q_1\star(\tilde Q_1\star\tilde Q_2)=\vec e_z$ and $(\tilde Q_1\star\tilde Q_1)\star\tilde Q_2=-\vec e_z$.
- **The paradox, and its resolution.** At the operator level the product is as well behaved as the plain one: the left multiplications associate in the reversed law, they form a monoid, and they carry the projectors of §*The Projectors* and the ideals of §*The Left Ideals*. The resolution is that the non-associativity of $\star$ is entirely carried by the **elements** and not by the operators, because the operators are plain operators with a conjugated index. This is the third specificity and the summary of the article: the quaternionic product is the structure in which the element theory and the operator theory differ maximally.

## Summary

The general quaternionic bilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ is the isotope of the plain product by the anti-automorphism in the first slot, so its left multiplication is the plain one with the conjugated index, $L_{\tilde Q_1}=L^{\mathrm{plain}}_{\tilde Q_1^{\natural}}$, and its operators are faithful linear images of the plain ones. Three consequences follow and constitute the specificities of the algebra. The operator $L_{\tilde Q_1}$ is a projector exactly when $\tilde Q_1$ is a plain idempotent, so the algebra has a family of projectors of complex dimension two while its own idempotents are $0$ and $e_t$ alone: it disowns them. The left ideals of the product coincide with the left ideals of the plain product, the minimal ones of complex dimension two, with the right and the two-sided theory absent. The square-zero operators are exactly those of the pure isotropic elements, while the nilpotents of the algebra are the whole zero-divisor cone of complex dimension three; the gap contains the plain idempotents, which are $\star$-nilpotents whose left multiplication is a projector, a combination the plain product forbids. At the operator level the algebra keeps the monoid and the operator calculus of the associative theory; at the element level it keeps its left unit, loses the right one, the centre and every associativity law.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | the general quaternionic product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ |
| juxtaposition | the plain associative product $\tilde Q_1\tilde Q_2$ |
| $L_{\tilde Q_1}$ | the left multiplication $\tilde Q_2\mapsto\tilde Q_1\star\tilde Q_2$, equal to the plain left multiplication by $\tilde Q_1^{\natural}$ |
| $\natural$, $*$, $\overline{\cdot}$ | the natural, the star and the coefficientwise conjugations, all fixing $e_t$ |
| $\langle\tilde Q\rangle_{\natural}$ | the norm, $\langle\tilde Q\rangle_{\natural}e_t=\tilde Q\tilde Q^{\natural}$, vanishing on the zero-divisor cone |
| pure, isotropic | vanishing scalar part; vanishing complex bilinear form on the vector part |
| $\tilde\Pi$ | a plain idempotent; its left multiplication is a projector |
| $\mathbb{B}$ | the complex space $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the isotopes of a multiplication and the left and right multiplications of a non-associative algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the idempotents, the Peirce decomposition and the left ideals of the associative model $M_2(\mathbb{C})$ to which the operators of the product reduce.
- *The Specificities of the Biquaternion Algebra* (`articles_maths/the-specificities-of-the-biquaternion-algebra.md`), for the criterion that selects the plain product and the table of the twelve structures.
- *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.md`), for the idempotents $0$ and $e_t$ and the displacement of the plain idempotents into the projectors of this article.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the cone, the two families and the annihilators.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.md`), for the nilpotent cone and the index two.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the norm and the one-sided equations.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the monoid of the left multiplications and the failure of the right family.
- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternioid-c-space.md`), for the definition of $\star$ and of the three companion products.
