# __The Specificities of the Algebra of the Reduced Biquaternions__

## Introduction

Of the eight algebraic structures that the reduced biquaternion complex space carries, exactly one makes it an associative unital algebra over $\mathbb{C}$: the **general plain product** $\breve Q_{1}\breve Q_{2}$, the multiplication of *Introduction to the Algebra of the Reduced Biquaternions*. Every unital result of this block belongs to it — the ideal theory and the Peirce decomposition of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, the unit group of *The Group of Units of the Algebra of the Reduced Biquaternions*, the forms of *The Forms of the Algebra of the Reduced Biquaternions*, the multiplication operators of *The Multiplication Operators of the Algebra of the Reduced Biquaternions*, the matrix model of *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* — and this article states the exact reason, in one identity, and then reads the theory that the identity unlocks.

The reason is **left alternativity**, the law $\breve Q_{1}(\breve Q_{1}\breve Q_{2})=(\breve Q_{1}\breve Q_{1})\breve Q_{2}$ at every pair; it is equivalent to the operator identity $L_{\breve Q}L_{\breve Q}=L_{\breve Q \breve Q}$, and it is the threshold at which the operator calculus of the block begins. It is strictly weaker than associativity, so it is the sharp statement, and it is the criterion that separates the plain product from the other seven. The reduced biquaternion case has one property the biquaternion case does not: the multiplication is **commutative**, so left alternativity and right alternativity coincide and the criterion is simply associativity. What the criterion opens, together with the commutativity, is the block's own subject matter: the **central idempotents** that split the algebra into the direct product of two fields, the two minimal ideals they carry, the vanishing off-diagonal of the Peirce decomposition, the reduced and semisimple structure, and the regular representation of the multiplication operators.

## The Criterion

**Definition (left alternativity).** A product $\circ$ on the complex space is **left-alternative** when
$$
\breve Q\circ(\breve Q\circ \breve Q_{2})=(\breve Q\circ \breve Q)\circ \breve Q_{2}\qquad\text{for all }\breve Q,\breve Q_{2}.
$$

**Theorem (the criterion).** For a product $\circ$ the operator identity
$$
\boxed{\;
L^{\circ}_{\breve Q}\circ L^{\circ}_{\breve Q}=L^{\circ}_{\breve Q\circ \breve Q}\qquad\text{for every }\breve Q
\;}
$$
holds exactly when $\circ$ is left-alternative.

*Proof.* Evaluate both sides at $\breve Q_{2}$: the left side is $\breve Q\circ(\breve Q\circ \breve Q_{2})$ and the right side is $(\breve Q\circ \breve Q)\circ \breve Q_{2}$. The two operators agree for all $\breve Q,\breve Q_{2}$ exactly when the two elements agree for all $\breve Q,\breve Q_{2}$, which is the definition of left alternativity.

**Corollary (idempotents and square-zero elements).** In a left-alternative structure every idempotent gives a **projector**, $L_{\Pi}^{2}=L_{\Pi}$, and every square-zero element gives a **square-zero operator**, $L_{\breve Q}^{2}=0$ when $\breve Q^{2}=0$.

*Proof.* By the theorem $L_{\Pi}^{2}=L_{\Pi\circ\Pi}=L_{\Pi}$ and $L_{\breve Q}^{2}=L_{\breve Q\circ \breve Q}=L_{0}=0$ for a square-zero element.

**Remark (commutativity collapses the two laws).** The mirror statement with the right multiplications characterizes right alternativity, and a product is associative exactly when the two laws hold together. For the plain product the commutativity gives $R_{\breve Q}=L_{\breve Q}$ at every element, so the two laws are the same statement; the criterion is therefore simply associativity here, and no one-sided distinction survives. This is the first specificity of the reduced biquaternion algebra against the biquaternion algebra, whose plain product is associative but not commutative.

## The Associative Interpretation

The block is the one structure where the full associative theory is available. This section states that theory in the block's own terms; each item is owned by an article of the block and cited.

### The Algebra and Its Idempotents

The plain product is associative, commutative, unital with unit $1$, and $\mathbb{C}$-bilinear, so $\mathbb{B}_{\mathrm{r}}$ is a commutative associative unital $\mathbb{C}$-algebra. It is the **direct product of two copies of $\mathbb{C}$**,
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-,\qquad \Pi_+^{2}=\Pi_+,\quad \Pi_-^{2}=\Pi_-,\quad \Pi_+\Pi_-=0,\quad \Pi_++\Pi_-=1,
$$
the two idempotents being **central** because the algebra is commutative. The isomorphism is the idempotent coordinate map $\breve Q\mapsto(Q_{+},Q_{-})$, which is an algebra isomorphism $(\mathbb{B}_{\mathrm{r}},\cdot)\to\mathbb{C}\times\mathbb{C}$:
$$
\breve Q_{1}\breve Q_{2}=Q_{1+}Q_{2+}\,\Pi_++Q_{1-}Q_{2-}\,\Pi_-.
$$
The scalar line $\mathbb{C}\cdot 1$ is the **diagonal** $\{(Q_{+},Q_{+})\}$, not the centre — the ring centre of a commutative algebra is the whole algebra — and the two idempotent lines are the two coordinate factors.

### The Ideals and the Peirce Decomposition

Because the algebra is a direct product of two fields it is **semisimple and not simple**: its only ideals are
$$
0,\qquad \mathbb{C}\Pi_+,\qquad \mathbb{C}\Pi_-,\qquad \mathbb{B}_{\mathrm{r}},
$$
the two middle ones **minimal**, and because the algebra is commutative the left, the right and the two-sided ideals coincide. The minimal ideals are generated by their idempotents, $\mathbb{C}\Pi_+=\mathbb{B}_{\mathrm{r}}\Pi_+$ and $\mathbb{C}\Pi_-=\mathbb{B}_{\mathrm{r}}\Pi_-$, and the ideal lattice is the two-element chain completed by the two incomparable middle terms. The ideal theory and the Peirce decomposition are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*.

For the idempotent pair $\Pi_+,\Pi_-$, with $\Pi_-=1-\Pi_+$, the **Peirce decomposition** is
$$
\boxed{\;
\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--},\qquad
\mathbb{B}_{\sigma\tau}=\{\breve Q:\Pi_\sigma \breve Q\Pi_\tau=\breve Q\},\qquad \sigma,\tau\in\{+,-\}
\;},
$$
and here it is **diagonal**: because the idempotents are central and orthogonal,
$$
\boxed{\; \mathbb{B}_{+-}=\Pi_+\mathbb{B}_{\mathrm{r}}\Pi_-=\mathbb{B}_{\mathrm{r}}\Pi_+\Pi_-=0,\qquad \mathbb{B}_{-+}=0 \;},
$$
so the decomposition reduces to the direct product $\mathbb{B}_{++}\oplus\mathbb{B}_{--}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$. This is the sharp contrast with the biquaternion Peirce theory, whose off-diagonal spaces are the one-dimensional matrix-unit spaces $E_{12},E_{21}$ of $M_2(\mathbb{C})$; the reduced biquaternion has no off-diagonal because its idempotents are central.

### The Module Theory and the Enveloping Algebra

Because $\mathbb{B}_{\mathrm{r}}$ is associative and unital, its left modules are its representations, so the ideal theory and the module theory are one subject. The algebra is a direct product of two fields, hence **semisimple and Morita-trivial**: every module is semisimple, the simple modules are the two coordinate lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ with their two characters, and every finitely generated module is a direct sum of copies of these two. The **enveloping operator algebra** is generated by the left and the right multiplications, and because the algebra is commutative every sandwich operator is a left multiplication, $L_{\breve Q_{1}}R_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$, so the image of $\mathbb{B}_{\mathrm{r}}^{\mathrm e}$ in $\mathrm{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$ is the two-dimensional space $\{L_{\breve Q}:\breve Q\in\mathbb{B}_{\mathrm{r}}\}$ and not the whole of $\mathrm{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})\cong M_{2}(\mathbb{C})$. The multiplication operators and the bi-module structure are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*.

## What the Criterion Delivers

The criterion of §*The Criterion* is the exact statement of why the theory above is available in the block. Four consequences, each a theorem of the block.

- **The projector calculus.** Every idempotent gives a projector, so every idempotent splits the space as $\mathbb{B}_{\mathrm{r}}=\mathrm{im}\,L_{\Pi}\oplus\ker L_{\Pi}$; because the product is commutative and associative, the image is the principal ideal $\mathbb{B}_{\mathrm{r}}\Pi$, the kernel is the annihilator $\mathrm{ann}(\Pi)$, and the two are the two lines of the other idempotent. In a structure without the criterion an idempotent still gives a fixed set of $L_{\Pi}$, but not a complement.
- **The square-zero operators vanish.** The multiplication has no nonzero square-zero element — it is reduced, by *Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions* — so the flag construction of the nilpotents is empty here. The elements whose operators are square-zero are exactly the elements whose square is $0$, namely $0$ alone.
- **The central splitting.** Because $\Pi_+$ and $\Pi_-$ are central idempotents, the projectors $L_{\Pi_+}$ and $L_{\Pi_-}$ are **algebra** projections: the images $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are subalgebras, and the decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ is a decomposition of algebras, not only of vector spaces. The decomposition is an algebra decomposition exactly for the plain product; for the other three general products the idempotent coordinates do not multiply componentwise, and the split is not compatible with the product.
- **The module theory.** Because the algebra is associative and unital and commutative, the left modules are the representations, the two simple modules are the two coordinate characters, and the algebra is Morita-trivial; none of this survives the loss of the criterion.

## The Isolation among the Eight

One law separates the block from the other seven, and this section names it and the boundary.

**Theorem (the isolation).** Of the eight structures — the four general products and the four structures obtained from the two tessarine bilinear products by symmetrisation and antisymmetrisation, all of *The Four Products, Their Forms and Their Algebraic Norms* — the general plain product is the only one that is left-alternative, equivalently the only one whose multiplication operators satisfy $L^{\circ}_{\breve Q}L^{\circ}_{\breve Q}=L^{\circ}_{\breve Q\circ \breve Q}$ at every element, and the only one that is associative and unital.

*Proof.* The four general products are the general plain bilinear product $\breve Q_{1}\breve Q_{2}$, the general tessarine bilinear product $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$, the general plain sesquilinear product $\breve Q_{1}\breve Q_{2}^{*}$ and the general tessarine sesquilinear product $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$. The plain product is associative by the associativity of $\mathbb{C}$, with $1$ as two-sided unit. The other three fail the criterion, each with a witness on the two idempotent lines. For the general tessarine bilinear product take $\breve Q_{1}=\Pi_+$ and $\breve Q_{2}=\Pi_-$: on the one hand $\breve Q_{1,\mathrm{ts}}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})=\Pi_-\,(\Pi_-\Pi_-)=\Pi_-$, and on the other $(\breve Q_{1,\mathrm{ts}}\breve Q_{1})_{\mathrm{ts}}\breve Q_{2}$, whose inner factor is $\breve Q_{1,\mathrm{ts}}\breve Q_{1}=\Pi_-\Pi_+=0$, is $0$; the two sides differ, so the criterion fails. For the general plain sesquilinear product the second slot is read through the conjugate-linear star, so the criterion would equate a linear with a conjugate-linear operator and cannot hold at a nonzero element; for the general tessarine sesquilinear product both slots carry a conjugation and the failure combines. The four symmetrised and antisymmetrised structures inherit the failure: the symmetric ones are commutative but not associative, the antisymmetric ones are neither, and none of the four is left-alternative. The plain product alone keeps the law.

The isolation is about the **theorem** and not about isolated elements, and the distinction is the exact boundary of the claim. Single elements of the other structures do produce projectors — the plain idempotents give projectors under multiplication in some of the products — but no other structure carries the law, hence the class of its well-behaved elements is not a theory.

| family | structure | associative | unital | commutative |
|---|---|---|---|---|
| plain | the general plain bilinear product $\breve Q_{1}\breve Q_{2}$ | **yes** | **yes**, unit $1$ | **yes** |
| first slot ${}_{\mathrm{ts}}$ | the general tessarine bilinear product $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ | no | no ($\breve Q_{\mathrm{ts}}1=\breve Q_{\mathrm{ts}}$) | no, symmetric up to ${}_{\mathrm{ts}}$: $\breve Q_{2,\mathrm{ts}}\breve Q_{1}=(\breve Q_{1,\mathrm{ts}}\breve Q_{2})_{\mathrm{ts}}$ |
| second slot ${}^{*}$ | the general plain sesquilinear product $\breve Q_{1}\breve Q_{2}^{*}$ | no | no ($1\breve Q^{*}=\breve Q^{*}$) | no, symmetric up to ${}^{*}$: $\breve Q_{2}\breve Q_{1}^{*}=(\breve Q_{1}\breve Q_{2}^{*})^{*}$ |
| both slots | the general tessarine sesquilinear product $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ | no | no | no, symmetric up to $\bar{\cdot}$: $\breve Q_{2,\mathrm{ts}}\breve Q_{1}^{*}=\overline{\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}}$ |
| symmetric parts | of $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ and $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ | no | no | **yes** |
| antisymmetric parts | of $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ and $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ | no | no | no (alternating) |

## The Boundary of the Criterion

The one structure that comes closest is the **general tessarine sesquilinear product**, the boundary of the criterion. It is symmetric **up to the bar**, $\breve Q_{2,\mathrm{ts}}\breve Q_{1}^{*}=\overline{\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}}$, and its diagonal form is the layer's definite form $\langle\cdot\rangle_{\mathrm{ts}*}$ of *The Forms of the Algebra of the Reduced Biquaternions*; but it is not associative, so it does not share the criterion. Its multiplication operator is the plain $L_{\breve Q_{\mathrm{ts}}}$ composed with the star of the second slot,
$$
L_{\breve Q}=L_{\breve Q_{\mathrm{ts}}}\ \text{composed with the star of the second slot},
$$
so it inherits the projector calculus of the plain product for the elements fixed by the star, while it fails the criterion at the elements the star moves. The general tessarine sesquilinear product and the criteria it does and does not satisfy are *The Specificities of the General Quaternionic Sesqualgebra*, and it is named here only to locate the boundary: the plain product is the criterion, the general tessarine sesquilinear product is the nearest structure to it, and the remaining six are further. The symmetric halves are the other neighbours on the commutative side, but they carry no unit and no associativity at all, so the sesquilinear product, whose definite form and projector calculus survive on a large slice, is the closest of the seven.

## Summary

Of the eight structures on $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, the general plain product $\breve Q_{1}\breve Q_{2}$ is the only associative unital one, and the exact threshold of its theory is **left alternativity**, $\breve Q_{1}(\breve Q_{1}\breve Q_{2})=(\breve Q_{1}\breve Q_{1})\breve Q_{2}$ at every pair, equivalently $L_{\breve Q}L_{\breve Q}=L_{\breve Q \breve Q}$ at every element. Because the multiplication is commutative the right law coincides with the left one and the criterion is simply associativity. From the single identity, together with the commutativity, follow the projector calculus of the idempotents, the **central splitting** $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ into a direct product of two fields, the vanishing off-diagonal $\mathbb{B}_{+-}=\mathbb{B}_{-+}=0$ of the Peirce decomposition, the reduced and semisimple structure with its four ideals $0,\mathbb{C}\Pi_+,\mathbb{C}\Pi_-,\mathbb{B}_{\mathrm{r}}$, and the module theory with its two simple modules. The enveloping operator algebra acts through the left multiplications alone, so its image is the two-dimensional space $\{L_{\breve Q}\}$, not the whole endomorphism algebra. The criterion holds in the plain product and in no other of the eight: the general tessarine product fails through the tessarine sign in its first slot, the two sesquilinear products through the conjugate-linearity of the star, and the four halves inherit the failures of their parents. The isolation is a statement about the law and not about isolated elements, and the general tessarine sesquilinear product is the boundary case, the symmetric-up-to-the-bar but non-associative neighbour.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\breve Q_{1}\breve Q_{2}$ | the general plain product, the block's multiplication |
| $L_{\breve Q}:\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ | the left multiplication of the plain product |
| $\breve Q_{1}(\breve Q_{1}\breve Q_{2})=(\breve Q_{1}\breve Q_{1})\breve Q_{2}$ | left alternativity, the criterion |
| $L_{\breve Q}L_{\breve Q}=L_{\breve Q \breve Q}$ | the operator identity, equivalent to the criterion |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\ Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | the idempotent coordinates, with $\breve Q_{1}\breve Q_{2}=Q_{1+}Q_{2+}\Pi_++Q_{1-}Q_{2-}\Pi_-$ |
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ | the central algebra splitting |
| $\mathbb{B}_{\sigma\tau}=\{\breve Q:\Pi_\sigma \breve Q\Pi_\tau=\breve Q\}$ | the Peirce spaces, with $\sigma,\tau\in\{+,-\}$ and $\mathbb{B}_{+-}=\mathbb{B}_{-+}=0$ |
| $\mathrm{ann}(\Pi)$ | the annihilator of an idempotent, the other coordinate line |
| $\{L_{\breve Q}:\breve Q\in\mathbb{B}_{\mathrm{r}}\}$ | the image of the enveloping operator algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corner subalgebras of a finite-dimensional associative algebra.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for left alternativity and the alternative laws.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the ideal lattice and the Peirce decomposition.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the operators and the bi-module structure.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the unit group and its boundary.
- [The Specificities of the Biquaternion Algebra](the-specificities-of-the-biquaternion-algebra.html), for the non-commutative companion and the same criterion.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the eight structures and the isolation.
