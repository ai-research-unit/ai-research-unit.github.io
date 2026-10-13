# __The Operators of the Quaternionic Sesquilinear Product and the Indefinite Gauge Metric__

## Introduction

The GQS band reads the general quaternionic sesquilinear product as the **gauge** structure of the framework. The product is the fourth of the four general products of the biquaternion complex space,

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*},
$$

the plain product with the natural conjugation in the first slot and the Hermitian conjugation in the second. Its scalar part is an indefinite Hermitian form, the Krein form $K$ of signature $(1,3)$, and that one fact decides the whole operator layer of the band. Because the form is indefinite, the adjoint of the band is the **J-adjoint** — the adjoint for $K$ — and it is **not** the Hermitian adjoint for which the observables and the gauge generators of the probability band are read. There are therefore **two notions of self-adjointness** on the same operator, one for the indefinite form and one for the definite form, and the article is about exactly that difference.

The answer to the question the twelve bands ask is one sentence. The form of the band is the indefinite Krein form $K$, its adjoint is the J-adjoint

$$
T^{\dagger}=J\,T^{*}J,
$$

and on a one-sided multiplication the J-adjoint **swaps the sides and conjugates the parameter**,

$$
\bigl(L_{\tilde Q}\bigr)^{\dagger}=R_{\bar{\tilde Q}},
$$

where the definite Hermitian adjoint keeps the side. The two self-adjointnesses therefore part, and a J-self-adjoint operator need not be self-adjoint: the article writes down an explicit operator that is J-self-adjoint and skew-adjoint for the positive form at once.

The article carries the operator layer of the band and defers the rest. The metric itself is *The Fourth Product and Its Indefinite Metric*; the pure states that the metric cannot normalise are *The States the Indefinite Metric Cannot Normalise*; the no-go statement that the band is a gauge structure and not a state space is *Why the Fourth Product Is a Gauge Structure and Not a State Space*. The mathematics is owned by *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* for the indefinite adjoint and its types, by *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* for the two families and their composition, and by *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions* for the sandwich of the indefinite form; those facts are applied and verified here, never re-proved. The article reads against the composition band, *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*, where the adjoint is a transpose that swaps the sides, and against the probability band, where the adjoint is the definite Hermitian adjoint that conjugates the parameter and keeps the side.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$ and $e_1e_2=e_3$, and central $i$ with $i^{2}=-1$; an element is $\tilde Q=Q_0e_0+\mathbf Q$ with complex coefficients $Q_\mu$. Juxtaposition is the plain, associative product. The conjugations are the coefficientwise bar $\bar{\cdot}$, the natural conjugation ${}^{\natural}$ fixing $i$ and negating $e_1,e_2,e_3$, and the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so that $Q^{*}_{\nu}=\varepsilon_{\nu}\overline{Q_{\nu}}$ with the sign vector $\varepsilon=(1,-1,-1,-1)$. The sectors are $\mathbb{M}_+=\{\tilde Q^{*}=\tilde Q\}$ and $\mathbb{M}_-=\{\tilde Q^{*}=-\tilde Q\}$; $\mathbb{C}_{\mathbb{B}}$ is the centre and $\mathbb{V}_{\mathbb{B}}$ the vector subspace. The scalar part is $\mathrm{Sc}$, the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The two forms are the **definite** Hermitian form $(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{*}\tilde Q)=\sum_\mu\overline{P_\mu}Q_\mu$, positive definite of signature $(4,0)$, and the **indefinite** Krein form

$$
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

Hermitian, non-degenerate and indefinite of signature $(1,3)$. The fundamental symmetry is $J={}^{\natural}$, the $\mathbb{C}$-linear involution of matrix $E=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis, self-adjoint for both forms. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Two Multiplication Operators and Their Composition Law

The fourth product attaches one operator to each slot, and the two are not of the same kind.

**Definition (the multiplications of the product).** For $\tilde A\in\mathbb{B}$ the **left multiplication** and the **right multiplication** of the product $\star$ are

$$
L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X=\tilde A^{\natural}\tilde X^{*},\qquad
R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A=\tilde X^{\natural}\tilde A^{*}.
$$

They are the biquaternion instance of the two multiplication operators of a sesqualgebra, and their biquaternion determination is *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, which owns the two families, their parities and their composition. Alongside them the article uses the **plain one-sided operators**, $L_{\tilde P}(\tilde X)=\tilde P\tilde X$ and $R_{\tilde P}(\tilde X)=\tilde X\tilde P$, the operators of the general plain bilinear product, named as in *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*. The two pairs are related by the conjugations,

$$
L^{\star}_{\tilde A}=L_{\tilde A^{\natural}}\circ{}^{*},\qquad
R^{\star}_{\tilde A}=R_{\tilde A^{*}}\circ{}^{\natural}.
$$

**A notation mark.** The mathematics block writes the multiplications of its own product $L_{\tilde A},R_{\tilde A}$, and the physics blocks reserve the mark $\star$ for the fourth product, as *The Operators of the Symmetric Quaternionic Sesquilinear Product and the Gauge Metric* records; this article writes $L^{\star}_{\tilde A},R^{\star}_{\tilde A}$ for the band's two multiplications and gives the ordinary operators the unmarked names $L_{\tilde A},R_{\tilde A}$. The reader moving between the blocks should carry the code $\mathrm{GQS}$, not the marks.

**Proposition (the parities).** For every $\lambda\in\mathbb{C}$ and every $\tilde X\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L^{\star}_{\tilde A}(\tilde X),\qquad
R^{\star}_{\tilde A}(\lambda\tilde X)=\lambda\,R^{\star}_{\tilde A}(\tilde X),
$$

and for the parametrisations $L^{\star}_{\tilde A+\lambda\tilde B}=L^{\star}_{\tilde A}+\lambda L^{\star}_{\tilde B}$ and $R^{\star}_{\tilde A+\lambda\tilde B}=R^{\star}_{\tilde A}+\overline{\lambda}R^{\star}_{\tilde B}$.

*Proof.* The star is conjugate-linear and the natural conjugation is $\mathbb{C}$-linear, and both are anti-automorphisms; the two displays are the definitions read off. The ownership is *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, §*The Parities*.

**Read as a physical statement.** The two slots of the band's pairing have opposite polarity, and the multiplication operators inherit it. Attaching on the left conjugates the variable, because the left multiplication reads the second slot where the star sits; attaching on the right is linear, because the right multiplication reads the first slot where the natural conjugation sits, and that conjugation is $\mathbb{C}$-linear. A bilinear product reads both slots the same way, so no bilinear row of the twelve has this behaviour. This is an interpretation: it names the algebraic fact that the product is conjugate-linear in one argument and linear in the other, and it calls that polarity the two slots of a gauge pairing.

**Theorem (the composition law).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A^{\natural},\overline{\tilde B}},\qquad
R^{\star}_{\tilde A}R^{\star}_{\tilde B}=T_{\overline{\tilde B},\tilde A^{*}},
$$

where $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ is the ordinary two-sided operator; and the mixed composites are

$$
L^{\star}_{\tilde A}R^{\star}_{\tilde B}(\tilde X)=\tilde A^{\natural}\tilde B\,\overline{\tilde X},\qquad
R^{\star}_{\tilde B}L^{\star}_{\tilde A}(\tilde X)=\overline{\tilde X}\,\tilde A\tilde B^{*}.
$$

*Proof.* Each law is a two-line computation with the anti-automorphism properties $(UV)^{\natural}=V^{\natural}U^{\natural}$ and $(UV)^{*}=V^{*}U^{*}$, and they are proved in *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, §*The Composition of Two Left Multiplications* for the left law and §*The Other Compositions* for the right and the mixed laws. For the first, $L^{\star}_{\tilde A}L^{\star}_{\tilde B}(\tilde X)=\tilde A^{\natural}(\tilde B^{\natural}\tilde X^{*})^{*}=\tilde A^{\natural}\tilde X\overline{\tilde B}$; the others are the same computation on the other slot. Verified on sixty random pairs to machine precision.

**Corollary (no monoid, no single representation).** The composite of two left multiplications is a $\mathbb{C}$-linear operator, whereas every left multiplication is conjugate-linear; so the left family is not closed under composition and is not a monoid. In particular $L^{\star}_{\tilde A}=S_{\tilde A^{\natural},e_0}$ is the sesquilinear sandwich with parameters $\tilde A^{\natural}$ and $e_0$, and the sandwiches and the ordinary two-sided multiplications together form the monoid of *The Sesquilinear Sandwich Operator*. The right family does not close either, its composite being the two-sided operator $T_{\overline{\tilde B},\tilde A^{*}}$; and at the unit candidate,

$$
L^{\star}_{e_0}={}^{*},\qquad R^{\star}_{e_0}={}^{\natural},\qquad
L^{\star}_{e_0}R^{\star}_{e_0}=R^{\star}_{e_0}L^{\star}_{e_0}=\bar{\cdot},
$$

the coefficientwise conjugation, so neither family contains the identity.

**Read as a physical statement.** The band's operator families are not an algebra of the associative kind: they carry the two actions of the product, and their composites are the plain two-sided operations. The left family fixes nothing under composition, because a conjugate-linear family cannot multiply into itself; the right family likewise leaves the class, and the identity is reached only as the square of the left multiplication by the unit candidate. This is the operator form of the statement, owned by the sibling *Why the Fourth Product Is a Gauge Structure and Not a State Space*, that the fourth product is a structure of transformations and not a state space: a transformation structure need not compose into a monoid, and here it does not. This is an interpretation.

### The Norm of the Quaternionic Family

**Proposition (the natural quadratic form).** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_0,\qquad N(\tilde Q)=\sum_{\mu}Q_{\mu}^{2},
$$

the biquaternion norm, and for the left multiplication by a nontrivial idempotent $\tilde\Pi$ of the product, $L^{\star}_{\tilde\Pi}(\tilde\Pi^{\natural})=N(\tilde\Pi)e_0$.

*Proof.* The identity is $\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=N(\tilde Q)$ with vanishing vector part, *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*; the second is the idempotent proposition of *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, §*The Idempotents and the Units*.

**Read as a physical statement.** The norm enters the band exactly as it enters the whole quaternionic family: through the identity that pairs an element with its natural conjugate to a central scalar. Its modulus is what a J-unitary criterion measures, as the next sections show, and its vanishing locus is the zero-divisor cone that the gauge interpretation inherits. This is an interpretation of the identity, not a new computation.

## The Adjoint: the Indefinite Form and the J-Adjoint

The form decides the adjoint, and the form of the band is indefinite.

**Definition (the J-adjoint).** Let ${}^{*}$ be the adjoint for the definite form $(\cdot,\cdot)$, so that $T^{*}$ is the conjugate transpose in the coefficient basis. The **J-adjoint** is

$$
T^{\dagger}=J\,T^{*}J,
$$

the unique operator with $K(T\tilde P,\tilde Q)=K(\tilde P,T^{\dagger}\tilde Q)$ for all $\tilde P,\tilde Q$.

*Proof.* Existence and uniqueness are the non-degeneracy of $K$ in finite dimension; the characterisation in the coefficient basis is $T^{\dagger}=ETE$ with $E=\mathrm{diag}(1,-1,-1,-1)$. The ownership is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, §*The J-Adjoint*, verified there and on fifty random pairs here.

**Proposition (the calculus).** The J-adjoint is involutive, $(T^{\dagger})^{\dagger}=T$, and antimultiplicative with conjugated scalars,

$$
(TS)^{\dagger}=S^{\dagger}T^{\dagger},\qquad
(\alpha T+\beta S)^{\dagger}=\bar\alpha\,T^{\dagger}+\bar\beta\,S^{\dagger}.
$$

*Proof.* $J^{2}=\mathrm{id}$ and $T\mapsto T^{*}$ is an involution and an anti-involution; the scalar conjugation is the conjugate-linearity of ${}^{*}$. Ownership as above.

**Theorem (the adjoints of the families).** For all $\tilde Q,\tilde R\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q}\bigr)^{\dagger}=R_{\bar{\tilde Q}},\qquad
\bigl(R_{\tilde R}\bigr)^{\dagger}=L_{\bar{\tilde R}},\qquad
\bigl(L_{\tilde Q}R_{\tilde R}\bigr)^{\dagger}=L_{\bar{\tilde R}}R_{\bar{\tilde Q}},\qquad
\bigl(\Theta_{\tilde Q}\bigr)^{\dagger}=\Theta_{{}^{\natural}\tilde Q},
$$

where $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is the definite sandwich of the plain product. The J-adjoint of a **left** multiplication is a **right** multiplication: it swaps the sides and carries the parameter to its coefficient conjugate.

*Proof.* The natural conjugation is the anti-automorphism ${}^{\natural}L_{\tilde Q}{}^{\natural}=R_{\tilde Q^{\natural}}$, so $(L_{\tilde Q})^{\dagger}={}^{\natural}L_{\tilde Q}^{*}{}^{\natural}={}^{\natural}L_{\tilde Q^{*}}{}^{\natural}=R_{\tilde Q^{*\natural}}=R_{\bar{\tilde Q}}$; the second is the mirror; the third follows by antimultiplicativity, $(L_{\tilde Q}R_{\tilde R})^{\dagger}=R_{\tilde R}^{\dagger}L_{\tilde Q}^{\dagger}=L_{\bar{\tilde R}}R_{\bar{\tilde Q}}$; and for the sandwich, $(\Theta_{\tilde Q})^{\dagger}=R_{\tilde Q^{*}}^{\dagger}L_{\tilde Q}^{\dagger}=L_{\overline{\tilde Q^{*}}}R_{\bar{\tilde Q}}=\Theta_{{}^{\natural}\tilde Q}$. Ownership is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, §*The J-Adjoint of the Three Families*. Verified on sixty random parameters each.

**Read as a physical statement.** The band's adjoint is a transport of the side, and the transport conjugates the parameter on the way across. Where the composition band's transpose swaps the sides and leaves the parameter alone, and where the probability band's Hermitian adjoint conjugates the parameter and leaves the side, the adjoint of the indefinite form does both at once. The reason is the fundamental symmetry: the form $K$ is the definite form twisted by $J$, and $J$ is the natural conjugation, so the conjugation of the parameter is the trace of the twist. What the J-adjoint **measures** is the pairing of an operator against the indefinite metric: it is the operator that carries the metric from the first slot to the second, $K(T\tilde P,\tilde Q)=K(\tilde P,T^{\dagger}\tilde Q)$, and only for an operator equal to its own J-adjoint do the two interpretations of the metric through that operator agree. This is an interpretation of the theorem.

**Corollary (the adjoint of the band's own right multiplication).** The right multiplication of the band is $\mathbb{C}$-linear and has the J-adjoint

$$
\bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}=R^{\star}_{\tilde A^{*}},
$$

which **keeps the side** and conjugates the parameter. The left multiplication is conjugate-linear and does not belong to the linear adjoint calculus; it is the sandwich $S_{\tilde A^{\natural},e_0}$, whose sesquilinear adjoint is owned by *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*.

*Proof.* $R^{\star}_{\tilde A}=R_{\tilde A^{*}}\circ{}^{\natural}$, and ${}^{\natural}$ is J-self-adjoint, so $(R^{\star}_{\tilde A})^{\dagger}={}^{\natural}\circ(R_{\tilde A^{*}})^{\dagger}={}^{\natural}\circ L_{\bar{\tilde A^{*}}}={}^{\natural}\circ L_{\tilde A^{\natural}}=R_{\tilde A}\circ{}^{\natural}=R^{\star}_{\tilde A^{*}}$. Verified on sixty random parameters.

**Read as a physical statement.** The band's right multiplication already carries the twist, so its adjoint stays on its own side. The left multiplication does not, and its adjoint is a conjugate-linear object outside the linear theory. This is the operator reason that a sesquilinear row has no single representation: one of its two families lies outside the endomorphism algebra, and its adjoint does too. This is an interpretation.

### The Two Notions of Self-Adjointness

**Corollary (the definite–indefinite dictionary).** For every operator $T$,

$$
T^{\dagger}=T\iff (JT)^{*}=JT,\qquad
T^{\dagger}=-T\iff (JT)^{*}=-JT,
$$

so $T\mapsto JT$ is a bijection from the J-self-adjoint operators onto the self-adjoint operators of the definite form, and likewise for the skew families.

*Proof.* $T^{\dagger}=T\iff JT^{*}J=T\iff T^{*}J=JT\iff (JT)^{*}=T^{*}J^{*}=T^{*}J=JT$, using $J^{*}=J$ and $J^{2}=\mathrm{id}$. Ownership is the corollary of *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*. Verified on sixty random operators.

**Theorem (a J-self-adjoint operator that is not self-adjoint).** The operator

$$
W=L_{e_1}+R_{e_1},\qquad
W=\begin{pmatrix}0&-2&0&0\\2&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

in the coefficient basis, is J-self-adjoint, $W^{\dagger}=W$, and is **skew-adjoint** for the definite form, $W^{*}=-W$. Its spectrum is $\{2i,-2i,0\}$, non-real.

*Proof.* $(L_{e_1})^{\dagger}=R_{\bar{e_1}}=R_{e_1}$ and $(R_{e_1})^{\dagger}=L_{e_1}$, so the sum is J-self-adjoint. For the definite form the plain adjoints keep the side and conjugate the parameter, $(L_{\tilde Q})^{*}=L_{\tilde Q^{*}}$ and $(R_{\tilde Q})^{*}=R_{\tilde Q^{*}}$, so $(L_{e_1})^{*}=L_{-e_1}$ and $(R_{e_1})^{*}=R_{-e_1}$, and the sum is the negative of its own adjoint. The matrix is the sum of the two plain multiplications on the basis, and it has a single $2\times2$ block with eigenvalues $\pm 2i$. Verified by direct computation. The mixed-spectrum example is the one recorded in *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, §*The Indefinite Spectral Data*.

**Read as a physical statement.** J-self-adjointness is not self-adjointness, and the two cannot be identified by relabelling. The witness $W$ is J-self-adjoint and skew-adjoint for the positive form simultaneously, so no positive-definite form makes it self-adjoint; its non-real spectrum is the obstruction. The interpretation is that the band's self-adjointness is a statement about the **indefinite** form alone, and that interpretation an observable of the gauge band with the definite Hermitian adjoint would misclassify every one of its generators. This is an interpretation of the theorem.

## The Types of the Operators

The J-adjoint of a one-sided plain operator swaps the sides, and the left and the right families meet only at a central parameter, so the type criteria are criteria on one parameter again; the sandwich criterion is a criterion on the support of its parameter.

**Theorem (the J-types of the one-sided operators).** For $\tilde Q\in\mathbb{B}$,

$$
L_{\tilde Q}\ \text{is }J\text{-self-adjoint}\iff\tilde Q\in\mathbb{R}e_0,\qquad
L_{\tilde Q}\ \text{is }J\text{-skew-adjoint}\iff\tilde Q\in i\mathbb{R}e_0,
$$

and the same two criteria hold for $R_{\tilde R}$. For the band's own right multiplication, $R^{\star}_{\tilde A}$ is J-self-adjoint if and only if $\tilde A$ is Hermitian, $\tilde A\in\mathbb{M}_+$.

*Proof.* By the adjoint theorem, $L_{\tilde Q}$ J-self-adjoint is $R_{\bar{\tilde Q}}=L_{\tilde Q}$; the two families meet only at a central parameter, $L_{\tilde X}=R_{\tilde X}$ for $\tilde X$ central, so $\bar{\tilde Q}=\tilde Q$ and $\tilde Q\in\mathbb{C}_{\mathbb{B}}$ with $\tilde Q$ central; and a central element with $\bar{\tilde Q}=\tilde Q$ is real, so $\tilde Q\in\mathbb{R}e_0$. The skew case is $R_{\bar{\tilde Q}}=-L_{\tilde Q}$, which forces the central parameter to be purely imaginary. For the band's right multiplication, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$ and the parametrisation is injective, so self-adjointness is $\tilde A^{*}=\tilde A$. Ownership is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, §*The J-Adjoint of the Three Families*, checked there and on the basis here; the right-multiplication criterion was checked on sixty random parameters.

**Theorem (the J-types of the sandwich).** The definite sandwich is J-self-adjoint exactly on the union of the centre and the vector subspace,

$$
\Theta_{\tilde Q}\ \text{is }J\text{-self-adjoint}\iff\tilde Q\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}},
$$

and it is never J-skew-adjoint for a nonzero parameter.

*Proof.* $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$, and $\Theta_{\tilde S}=\Theta_{\tilde Q}$ exactly when $\tilde S=\lambda\tilde Q$ with $\lambda$ a central phase; then ${}^{\natural}\tilde Q=\lambda\tilde Q$ is the decomposition of the parameter into its scalar and its vector part with opposite signs, which holds exactly when one of the two parts vanishes. The skew case would need ${}^{\natural}\tilde Q=-\tilde Q$ on both parts or on the appropriate one, which forces $\tilde Q=0$. Ownership as above.

**Read as a physical statement.** The types of the band are cut out by the two eigenspaces of the fundamental symmetry, so the gauge observables are the real central multiplications and the gauge generators are the imaginary ones, while the sandwich is J-self-adjoint exactly on the two pure sign sectors of $J$. On the sandwich the criterion is not a criterion on a sector sign but on the **support** of the parameter: a sandwich by a parameter that is purely central or purely vector is J-self-adjoint, and a generically mixed parameter is not. This is an interpretation of the two theorems.

**Remark (the distinct real spectrum of the sandwich).** For a J-self-adjoint sandwich the spectrum is real with signs: $\{|\zeta|^{2}\}$ with multiplicity four for a central parameter $\tilde Q=\zeta e_0$, the pair $\pm\lvert N(\tilde Q)\rvert$ with multiplicity two each for a vector parameter of nonzero norm, and $\{0\}$ for a null vector; and a J-self-adjoint operator of the one-sided family is a real scalar multiple of the identity, with spectrum real. The spectral computations are *The Indefinite Spectra of the Operators on the Biquaternion Algebra* (mathematics) and are not re-derived here.

## The Symmetries of the Form and of the Product

**Theorem (the J-unitary operators, and the invariance of the indefinite form).** An invertible operator $T$ preserves the Krein form,

$$
K(T\tilde P,T\tilde Q)=K(\tilde P,\tilde Q)\qquad\text{for all }\tilde P,\tilde Q,
$$

if and only if $T^{\dagger}T=\mathrm{id}$, equivalently $T^{*}JT=J$. These are the **J-unitary** operators, and they form the indefinite unitary group

$$
U_{J}(\mathbb{B})=\{T:T^{*}JT=J\}\cong U(1,3),
$$

of real dimension sixteen, with maximal compact part $U(1)\times U(3)$.

*Proof.* $K(T\tilde P,T\tilde Q)=K(\tilde P,T^{\dagger}T\tilde Q)$ by the characterisation of the adjoint, so preservation is $T^{\dagger}T=\mathrm{id}$; in the coefficient basis this is $T^{*}ET=E$, the defining equation of the automorphism group of an indefinite form of signature $(1,3)$. Ownership is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, §*The J-Adjoint*, Corollary, and *The Krein Isometry Group and Its J-Contractions*.

**Corollary (the J-unitary operators of the band's families).** The J-unitary operators among the plain left and right multiplications are exactly the central phases,

$$
L_{\tilde Q}\ \text{is }J\text{-unitary}\iff\tilde Q\in S^{1}e_0,
$$

and the J-unitary operators among the sandwiches are exactly the norm-one slice,

$$
\Theta_{\tilde Q}\ \text{is }J\text{-unitary}\iff\lvert N(\tilde Q)\rvert=1,\qquad
\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{N(\tilde Q)e_0},
$$

with inverse $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$ on that slice. The J-unitary operators that the three families supply form the subgroup $U(1)\times SO(3)$ of $U_{J}(\mathbb{B})$.

*Proof.* A left multiplication fixes the first slot, so it preserves $K$ only if it is a central phase, and a central phase does; the sandwich computation is $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{{}^{\natural}\tilde Q}\Theta_{\tilde Q}=\Theta_{{}^{\natural}\tilde Q\,\tilde Q}=\Theta_{N(\tilde Q)e_0}$, the last step being the norm identity of §*The Norm of the Quaternionic Family*, so J-unitarity is $\lvert N(\tilde Q)\rvert=1$; on that slice $\Theta_{\tilde Q}^{\dagger}=\Theta_{{}^{\natural}\tilde Q}=\Theta_{\tilde Q^{-1}}$ because $\tilde Q^{-1}=N(\tilde Q)^{-1}\tilde Q^{\natural}$. Ownership is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* and *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*. Verified on sixty random parameters for the sandwich criterion and on the central and vector examples for the one-sided criterion.

**Read as a physical statement.** The isometries of the band are the transformations that leave the indefinite metric invariant, and they split into two very different populations. A one-sided multiplication preserves the metric only as a central phase, the gauge transformation of the first kind; a sandwich preserves it whenever the modulus of its norm is one, and that is the norm-one slice that the corpus reads as the Lorentz-type transformations of the internal frame. The two populations do not exhaust the J-unitary group: $U_{J}(\mathbb{B})\cong U(1,3)$ is much larger than the part the band's own multiplications supply. The interpretation is that the band's metric is invariant under a group larger than its multiplications, and that the multiplications are the minimal inner apparatus. This is an interpretation.

**Theorem (the multiplicative operators).** An operator $T$ is multiplicative for the plain product,

$$
T(\tilde X\tilde Y)=(T\tilde X)(T\tilde Y)\qquad\text{for all }\tilde X,\tilde Y,
$$

and is J-unitary, if and only if it is an inner automorphism by a unitary element, $\mathrm{Ad}_{\tilde U}$ with $\tilde U\tilde U^{*}=e_0$. On the sandwich family the two adjoints again part: the definite sandwich $\Theta_{\tilde Q}$ is multiplicative in its argument exactly for a unitary parameter, $\tilde Q^{*}\tilde Q=e_0$, whereas the indefinite sandwich $H_{Q}$ is multiplicative exactly for a J-unitary parameter, $Q^{\dagger}Q=\mathrm{id}$.

*Proof.* The multiplicative operators are the automorphisms of the plain product, and $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is central simple, so its automorphisms are the inner ones $\mathrm{Ad}_{\tilde U}$; the inner automorphism $\mathrm{Ad}_{\tilde U}$ is J-unitary if and only if $\tilde U$ is unitary, which was checked on sixty random units. The definite-sandwich criterion is *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*, §*Contrast with the Definite Sandwich*, and the indefinite one is §*The Dagger Sandwich* of the same article. The product itself is not associative, so multiplicativity is stated for the plain product and not for $\star$, in agreement with the sibling *Why the Fourth Product Is a Gauge Structure and Not a State Space*. The natural conjugation is an anti-automorphism and is therefore not counted among the multiplicative operators.

**Read as a physical statement.** The operators that preserve both the metric and the multiplication are the relabellings of the internal frame, and they are the inner automorphisms by the metric-preserving units; a generic measure-preserving operator is not multiplicative. This is the operator form of the corpus's separation between a transformation that preserves a pairing and a transformation that also preserves the composition. This is an interpretation.

## The Operators Acting on the Gauge Space

The operators act on the algebra $\mathbb{B}$ itself, and the relevant structure is the indefinite pairing carried by that space.

**Proposition (the fundamental decomposition).** The Krein form splits the algebra as an orthogonal direct sum

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}},
$$

with $K$ positive definite on the centre, negative definite on the vector subspace, and signature $(1,3)$; the whole algebra carries the realified signature $(2,6)$. The null set $\{K=0\}$ is the isotropic cone of the band.

*Proof.* The centre and the vector subspace are the eigenspaces of $J$ with eigenvalues $+1$ and $-1$, and the form is the definite form twisted by the fundamental symmetry, $K(\tilde P,\tilde Q)=(J\tilde Q,\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^*)$, so the signs of the eigenvalues are the signs of the form on the two eigenspaces; the inertia is *The Krein Gram Matrix and the Restrictions of the Form*, the realified signature $(2,6)$ being its realification.

**Proposition (the action of the isometries).** A J-unitary operator preserves the fundamental decomposition up to a Krein-orthogonal congruence, preserves the isotropic cone, and acts on the state side as a transformation of the gauge orbit; the one-sided J-unitary operators are the central phases, the gauge transformations of the first kind, and the sandwich parameters of modulus one act as the transformations of the internal frame.

*Proof.* Preservation of $K$ preserves its isotropic set, so the null cone is invariant under $U_J(\mathbb{B})$; the identification of the subgroups is the corollary of §*The Symmetries of the Form and of the Product*. The state side, its cone and its pure states are *The Spinor Space as a Module and as a Hilbert Space*, *The Complementary Space of the Spinor Space and Its Physical Meaning* and *Mass, Rank and the Positivity of the Dagger*, and are used, not studied, here.

**Read as a physical statement.** The band's operators act on the gauge space, and the states of the framework are not the gauge space: they are the elements the indefinite metric cannot normalise, which is the sibling's statement. What the operators do on the state side is preserve the null cone and transport the pairing; what they do not do is select a positive subspace. The interpretation under **gauge** is this: an indefinite metric is a structure of admissible transformations, not of admissible states, because it assigns a sign to a direction and no positive weight to a state; the natural operators of such a structure are the **gauge generators**, the J-skew-adjoint operators, and the metric-preserving conjugations, not the observables. The negative-norm and null directions are the directions the metric cannot normalise, and they are the reason the band stops at a gauge structure. This is the article's central interpretation.

## The Indefinite Hermitian Sandwich

The sandwich of the indefinite form is not the definite sandwich, and the difference is the adjoint that forms it.

**Definition (the indefinite Hermitian sandwich).** For operators $Q,T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ the **indefinite Hermitian sandwich** is

$$
H_{Q}(T)=Q\,T\,Q^{\dagger},\qquad Q^{\dagger}=JQ^{*}J.
$$

It is the biquaternion instance of *The Hermitian Sandwich on a Krein Space*, and the indefinite counterpart of the definite sandwich $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$. The two must not be confused: the definite sandwich is always an operator of the family $\{\Theta_{\tilde Q}\}$ and is quadratic in its parameter; the indefinite sandwich uses the J-adjoint and is not of that family in general.

**Theorem (the laws of the indefinite sandwich).** For all operators $Q,S,T$,

$$
H_{Q}(T^{\dagger})=H_{Q}(T)^{\dagger},\qquad
H_{Q}\bigl(H_{S}(T)\bigr)=H_{QS}(T),\qquad
H_{Q}(ST)=H_{Q}(S)H_{Q}(T)\iff Q^{\dagger}Q=\mathrm{id},
$$

and for a complex scalar $\alpha$, $H_{\alpha Q}(T)=\lvert\alpha\rvert^{2}H_{Q}(T)$. For a J-unitary parameter the sandwich preserves the indefinite form to the twisted arguments,

$$
K\bigl(H_{Q}(T)\tilde W,H_{Q}(T)\tilde P\bigr)=K\bigl(TQ^{\dagger}\tilde W,TQ^{\dagger}\tilde P\bigr),
$$

and transports kernel and image as $\ker H_{Q}(T)=(Q^{\dagger})^{-1}\ker T$ and $\operatorname{im}H_{Q}(T)=Q\operatorname{im}T$.

*Proof.* The four laws are *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*, §*The Dagger Sandwich*, and the form-preservation and the transport of kernel and image are §*Preservation of the Form and of J-Positivity*, checked here on forty random operators each. The adjoint law is antimultiplicativity of ${}^{\dagger}$ with $Q^{\dagger\dagger}=Q$; the composition is associativity; the multiplicativity is the cancellation of the middle factor $Q^{\dagger}Q$; the parameter rule is the conjugate-linearity of the adjoint.

**Read as a physical statement.** The sandwich of the band conjugates an operator by a parameter and its J-adjoint, and it commutes with the adjunction of the argument: the adjoint of a conjugated operator is the conjugation of its adjoint. It composes in its parameter, and it is multiplicative in its argument exactly for a parameter that is a J-isometry, which is the metric-preserving case. The interpretation is that the indefinite sandwich is the band's apparatus for transporting operators across the indefinite pairing, and that only a metric-preserving parameter turns that transport into an algebra homomorphism. This is an interpretation.

**Theorem (the sandwich against the inner automorphism).** For a J-unitary parameter $Q$, $Q^{\dagger}=Q^{-1}$ and the indefinite sandwich **is** the inner automorphism

$$
H_{Q}(T)=Q\,T\,Q^{\dagger}=Q\,T\,Q^{-1}=\mathrm{Ad}_{Q}(T),
$$

and for a parameter that is not a J-isometry the sandwich is not multiplicative and is not an inner automorphism.

*Proof.* $Q^{\dagger}=Q^{-1}$ is the defining equation of a J-isometry, and the transport $T\mapsto QTQ^{-1}$ is an automorphism of the operator algebra; conversely an inner automorphism is multiplicative, and multiplicativity of $H_Q$ forces $Q^{\dagger}Q=\mathrm{id}$ by the multiplicativity law of §*The Indefinite Hermitian Sandwich*. The comparison with the definite sandwich is *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*, §*Contrast with the Definite Sandwich*.

**Read as a physical statement.** A metric-preserving conjugation is an inner automorphism of the operator algebra, and the conjugations that are not metric-preserving are not automorphisms at all. The interpretation is that the gauge group of the band acts on its own operators by conjugation, and that the metric-preservation is exactly what makes that action a symmetry of the algebra. This is an interpretation.

## A Worked Case

Take the vector parameter

$$
\tilde Q=e_1+2ie_2,\qquad N(\tilde Q)=1^{2}+(2i)^{2}=1-4=-3,\qquad
\tilde Q^{*}=e_1^{*}+2i\,e_2^{*}=-e_1+2ie_2 .
$$

The parameter lies in the vector subspace, so the sandwich $\Theta_{\tilde Q}$ is J-self-adjoint by the criterion, and it is **not** self-adjoint for the definite form: the definite adjoint is $\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}=\Theta_{-e_1+2ie_2}\neq\Theta_{\tilde Q}$, because $\tilde Q^{*}$ is not a phase multiple of $\tilde Q$ (the $e_1$ component forces the phase $-1$ and the $e_2$ component forces $+1$). The operator is J-unitary only if $\lvert N\rvert=1$, and here $\lvert N\rvert=3$, so it is not J-unitary either. The same parameter therefore separates the two notions of self-adjointness and shows that J-self-adjointness carries no unitarity.

Take next a **boost** parameter,

$$
\tilde\Lambda=\cosh u\,e_0+\sinh u\,ie_1,\qquad
N(\tilde\Lambda)=\cosh^{2}u-\sinh^{2}u=1,
$$

which is Hermitian, $\tilde\Lambda^{*}=\tilde\Lambda$, and lies in neither the centre nor the vector subspace, so its sandwich is **J-unitary and not J-self-adjoint**. On the two-dimensional sub-block spanned by $e_0,e_1$ the operator is

$$
\Theta_{\tilde\Lambda}=\begin{pmatrix}\cosh 2u&-i\sinh 2u\\ i\sinh 2u&\cosh 2u\end{pmatrix}\oplus\mathrm{I}_2
$$

in the coefficient basis of §*Conventions*, and it preserves the Krein form while changing the definite form: for $\tilde P=e_0$ one has $\Theta_{\tilde\Lambda}e_0=\cosh 2u\,e_0+i\sinh 2u\,e_1$ and

$$
K(\Theta_{\tilde\Lambda}e_0,\Theta_{\tilde\Lambda}e_0)=K(e_0,e_0)=1,\qquad
(\Theta_{\tilde\Lambda}e_0,\Theta_{\tilde\Lambda}e_0)=\cosh^{2}2u+\sinh^{2}2u=\cosh 4u>1 .
$$

The boost is thus a transformation of the internal frame and not an isometry of the state side, which is the operator form of the gauge interpretation.

Take finally the **witness** of the two self-adjointnesses,

$$
W=L_{e_1}+R_{e_1},\qquad
W=\begin{pmatrix}0&-2&0&0\\2&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

which is J-self-adjoint, $W^{\dagger}=W$, and skew-adjoint for the definite form, $W^{*}=-W$, so it is not self-adjoint; its spectrum is $\{2i,-2i,0\}$, non-real. The witness is the sharpest display of the band's distinction: a J-self-adjoint operator of the framework is not an observable of the positive form, and no choice of positive form repairs the mismatch.

**A numerical check.** The composition laws $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A^{\natural},\overline{\tilde B}}$ and $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=T_{\overline{\tilde B},\tilde A^{*}}$ and the two mixed laws were checked on sixty random pairs to machine precision; the sandwich identity $L^{\star}_{\tilde A}=S_{\tilde A^{\natural},e_0}$ on forty random pairs; the J-adjoints $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, $(R_{\tilde R})^{\dagger}=L_{\bar{\tilde R}}$, $(L_{\tilde Q}R_{\tilde R})^{\dagger}=L_{\bar{\tilde R}}R_{\bar{\tilde Q}}$, $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$ and $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$ on sixty random parameters each; the dictionary $(JT)^{*}=JT$ on sixty random operators; the J-types of the one-sided family on the central, pure, mixed and basis parameters and the right-multiplication criterion on sixty random parameters; the sandwich J-self-adjointness criterion on the centre, the vector subspace and the mixed parameters; the J-unitarity criterion $\lvert N\rvert=1$ on sixty random parameters; the norm identity $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$ and $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{N(\tilde Q)e_0}$; the indefinite-sandwich laws and the kernel and image transport on forty random operators; and the witness matrix, its J-self-adjointness, its definite skew-adjointness and its spectrum, all exact to machine precision.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must declare.

- **The composition laws are cited, not re-proved.** They are *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, §*The Composition of Two Left Multiplications* and §*The Other Compositions*, and the interpretation of a multiplication as a process is *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*.
- **The indefinite adjoint and its type criteria are applied, not derived.** They are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; the article verifies the formulas and reads them.
- **The indefinite sandwich is owned by its mathematics article.** *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions* owns the sandwich laws, the form-preservation, the transport of kernel and image and the contrast with the definite case; this article cites them and reads them.
- **The metric is not re-read here.** The form $K$, its inertia, its isometry group and the **physical interpretation** of the metric are *The Fourth Product and Its Indefinite Metric*; the null states are *The States the Indefinite Metric Cannot Normalise*; the no-go statement is *Why the Fourth Product Is a Gauge Structure and Not a State Space*.
- **The physical adjoint is not this adjoint.** The observables and the gauge generators of the framework are read with the **definite** Hermitian adjoint of the probability band, *Observables, Gauge Generators and the Chirality of the Internal Action*; this article's adjoint is the **indefinite** one and its fixed points are not the observables of the state side.
- **The state space is used, not studied.** The spinor module, its complement and the state cone are *The Spinor Space as a Module and as a Hilbert Space*, *The Complementary Space of the Spinor Space and Its Physical Meaning* and *Mass, Rank and the Positivity of the Dagger*.
- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article declares only the GQS column.

**What the framework does not claim.** The interpretation does not derive the gauge group, the Lorentz-type transformations or the indefinite metric from the operator calculus; it reads the structures the corpus already uses. It does not identify the J-self-adjoint operators with observables; it states that the observables are read with the definite adjoint, and that the two classes part. It does not claim that the band's multiplications exhaust the isometry group, which is $U(1,3)$ and strictly larger. And it does not claim that the indefinite metric is a state space; the state side is the definite form, as the sibling says.

## The Ledger

**Proved.** The two multiplications of the fourth product are $L^{\star}_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X^{*}$, conjugate-linear in the variable, and $R^{\star}_{\tilde A}(\tilde X)=\tilde X^{\natural}\tilde A^{*}$, complex-linear, with $L^{\star}_{\tilde A}=L_{\tilde A^{\natural}}\circ{}^{*}$ and $R^{\star}_{\tilde A}=R_{\tilde A^{*}}\circ{}^{\natural}$; their composition laws are $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A^{\natural},\overline{\tilde B}}$ and $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=T_{\overline{\tilde B},\tilde A^{*}}$, the mixed composites are $\tilde A^{\natural}\tilde B\overline{\tilde X}$ and $\overline{\tilde X}\tilde A\tilde B^{*}$, the left multiplication is the sandwich $S_{\tilde A^{\natural},e_0}$, and neither family is closed under composition, so the band has no monoid and no single representation. The form of the band is the indefinite Krein form $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ of signature $(1,3)$, and its adjoint is the J-adjoint $T^{\dagger}=JT^{*}J$, involutive and antimultiplicative, characterised by $K(T\tilde P,\tilde Q)=K(\tilde P,T^{\dagger}\tilde Q)$. On the families the J-adjoint swaps the sides and conjugates the parameter, $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, $(R_{\tilde R})^{\dagger}=L_{\bar{\tilde R}}$ and $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$, while the band's own right multiplication keeps the side, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$. The dictionary is that $T$ is J-self-adjoint exactly when $JT$ is self-adjoint; and there are explicit operators that are J-self-adjoint and not self-adjoint, the sum $W=L_{e_1}+R_{e_1}$ being skew-adjoint for the definite form with non-real spectrum $\{2i,-2i,0\}$. The J-types are $L_{\tilde Q}$ J-self-adjoint exactly for $\tilde Q\in\mathbb{R}e_0$ and J-skew-adjoint exactly for $\tilde Q\in i\mathbb{R}e_0$, the band's right multiplication J-self-adjoint exactly for $\tilde A$ Hermitian, and the sandwich J-self-adjoint exactly for a parameter in the centre or the vector subspace and never J-skew. The J-unitary operators preserve $K$ and form $U_{J}(\mathbb{B})\cong U(1,3)$; among the families they are the central phases for the one-sided multiplications and the norm-one slice $\lvert N\rvert=1$ for the sandwiches, with $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{N(\tilde Q)e_0}$; the common part is $U(1)\times SO(3)$. The indefinite Hermitian sandwich $H_{Q}(T)=QTQ^{\dagger}$ satisfies $H_{Q}(T^{\dagger})=H_{Q}(T)^{\dagger}$, composes as $H_{Q}(H_{S}(T))=H_{QS}(T)$, is multiplicative in its argument exactly for $Q^{\dagger}Q=\mathrm{id}$, scales as $\lvert\alpha\rvert^{2}$ in its parameter, preserves the indefinite form to the twisted arguments, transports kernel and image as $\ker H_{Q}(T)=(Q^{\dagger})^{-1}\ker T$ and $\operatorname{im}H_{Q}(T)=Q\operatorname{im}T$, and is an inner automorphism of the operator algebra for a J-unitary parameter.

**Interpretations.** That the adjoint of the band is taken for the **indefinite** form and is therefore the J-adjoint, which distinguishes it from the probability band and from the composition band; that the J-adjoint of a one-sided multiplication **swaps the sides and conjugates the parameter**, where the definite Hermitian adjoint keeps the side; that **J-self-adjointness is not self-adjointness**, the witness $W$ being J-self-adjoint and skew-adjoint for the positive form at once; that the natural operators of an indefinite metric are the **gauge generators**, the J-skew-adjoint operators, and the metric-preserving conjugations, not the observables of the state side; that the negative-norm and null directions are the directions the metric cannot normalise, so an indefinite metric is a **gauge structure and not a state space**; and that the norm enters the band's criteria through the identity $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$ and the modulus $\lvert N\rvert$. Each is the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

Read under the job word **gauge**, the article is the operator layer of an indefinite-metric theory. The form of the band is the Krein form, its isometry group is $U(1,3)$, and the adjoint it defines is the indefinite adjoint; the definite Hermitian adjoint with which the observables of the framework are read is a different operation on the same algebra, and the first interpretation is that an indefinite metric forces the two apart. The second interpretation is that the band's transformations are the metric-preserving ones: the central phases are the transformations of the first kind, the norm-one sandwiches are the transformations of the internal frame, and the full isometry group is larger than either. The third interpretation is negative and is the sharpest: the null and negative directions of the metric are exactly the directions a gauge metric cannot normalise, so the band is a structure of admissible transformations and not a structure of admissible states; the state side of the framework is the positive definite form. Read against the composition band and the probability band, the three rows of the sesquilinear and bilinear block are three different adjoints on one algebra: the transpose that swaps the sides without conjugating, the Hermitian adjoint that conjugates and keeps the side, and the J-adjoint that does both at once. The placement of the band in the twelve is the final interpretation: it is the indefinite row, the one where positivity fails and where the metric remains a metric.

## Summary

The GQS band has for its product the general quaternionic sesquilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$, and for its multiplication operators the conjugate-linear left multiplication $L^{\star}_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X^{*}$ and the complex-linear right multiplication $R^{\star}_{\tilde A}(\tilde X)=\tilde X^{\natural}\tilde A^{*}$. The left multiplication is the sandwich $S_{\tilde A^{\natural},e_0}$; the composition laws are $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A^{\natural},\overline{\tilde B}}$ and $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=T_{\overline{\tilde B},\tilde A^{*}}$, and neither family is closed under composition, so the band has no monoid and no single representation. The form of the band is the indefinite Krein form $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ of signature $(1,3)$, and its adjoint is the J-adjoint $T^{\dagger}=JT^{*}J$, in contrast with the definite Hermitian adjoint of the probability band and the transpose of the composition band. On the plain families the J-adjoint swaps the sides and conjugates the parameter, $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ and $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$; on the band's own right multiplication it keeps the side, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$. The dictionary is that $T$ is J-self-adjoint exactly when $JT$ is self-adjoint, so the two self-adjointnesses part: the operator $W=L_{e_1}+R_{e_1}$ is J-self-adjoint and skew-adjoint for the definite form, with non-real spectrum, and no positive form makes it self-adjoint. The J-types are the real central parameters for the J-self-adjoint one-sided operators and the imaginary ones for the J-skew; the sandwich is J-self-adjoint exactly on the centre or the vector subspace; and the J-unitary operators preserve $K$ and form $U(1,3)$, meeting the families in the central phases for the one-sided operators and the norm-one slice for the sandwiches, with the common part $U(1)\times SO(3)$. The indefinite Hermitian sandwich $H_{Q}(T)=QTQ^{\dagger}$ commutes with adjunction, composes in its parameter, is multiplicative exactly for a J-isometry, scales by the squared modulus of a scalar parameter, preserves the indefinite form to the twisted arguments, and is an inner automorphism for a J-unitary parameter. The worked case separates the notions on one element, the vector parameter $e_1+2ie_2$ being J-self-adjoint and neither self-adjoint nor J-unitary, and the boost $\cosh u\,e_0+\sinh u\,ie_1$ being J-unitary and not J-self-adjoint; the witness $W$ is the explicit proof that a J-self-adjoint operator need not be self-adjoint. The reading under gauge is that an indefinite metric is a structure of transformations and not of states, that its natural operators are the gauge generators and the metric-preserving conjugations, and that the null directions are the boundary of what the metric can normalise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | The general quaternionic sesquilinear product; the fourth product |
| $L^{\star}_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X^{*}$ | Left multiplication; conjugate-linear in the variable |
| $R^{\star}_{\tilde A}(\tilde X)=\tilde X^{\natural}\tilde A^{*}$ | Right multiplication; complex-linear in the variable |
| $L_{\tilde P}$, $R_{\tilde P}$ | The plain left and right multiplications, $\tilde P\tilde X$ and $\tilde X\tilde P$ |
| $L^{\star}_{\tilde A}=L_{\tilde A^{\natural}}\circ{}^{*}$, $R^{\star}_{\tilde A}=R_{\tilde A^{*}}\circ{}^{\natural}$ | The band's operators in the plain ones |
| $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ | The ordinary two-sided operator |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A^{\natural},\overline{\tilde B}}$, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=T_{\overline{\tilde B},\tilde A^{*}}$ | The composition laws; no monoid |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q$ | The sesquilinear sandwich; $L^{\star}_{\tilde A}=S_{\tilde A^{\natural},e_0}$ |
| $(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{*}\tilde Q)$ | The definite Hermitian form, signature $(4,0)$ |
| $K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ | The indefinite Krein form, signature $(1,3)$ |
| $J={}^{\natural}$, $E=\mathrm{diag}(1,-1,-1,-1)$ | The fundamental symmetry, $J^{2}=\mathrm{id}$, self-adjoint for both forms |
| $T^{\dagger}=JT^{*}J$ | The J-adjoint; $K(T\tilde P,\tilde Q)=K(\tilde P,T^{\dagger}\tilde Q)$ |
| $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, $(R_{\tilde R})^{\dagger}=L_{\bar{\tilde R}}$ | The J-adjoint swaps the sides and conjugates the parameter |
| $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$ | The J-adjoint of the sandwich and of the right multiplication |
| $T^{\dagger}=T\iff (JT)^{*}=JT$ | The definite–indefinite dictionary |
| $W=L_{e_1}+R_{e_1}$ | The witness: J-self-adjoint, definite-skew-adjoint, spectrum $\{2i,-2i,0\}$ |
| $L_{\tilde Q}$ J-self-adjoint $\iff\tilde Q\in\mathbb{R}e_0$; J-skew $\iff\tilde Q\in i\mathbb{R}e_0$ | The one-sided J-types |
| $\Theta_{\tilde Q}$ J-self-adjoint $\iff\tilde Q\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}}$ | The sandwich J-type |
| $U_{J}(\mathbb{B})\cong U(1,3)$ | The J-unitary group; real dimension sixteen; compact part $U(1)\times U(3)$ |
| $\Theta_{\tilde Q}$ J-unitary $\iff\lvert N(\tilde Q)\rvert=1$ | The norm-one slice; $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{N(\tilde Q)e_0}$ |
| $H_{Q}(T)=QTQ^{\dagger}$ | The indefinite Hermitian sandwich |
| $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=\sum_\mu Q_\mu^{2}$ | The biquaternion norm, central |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{V}_{\mathbb{B}}$, $\mathbb{M}_{\pm}$ | The centre, the vector subspace, the two sectors |

## Further Reading

- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the J-adjoint, the dictionary with the definite case, the type criteria, the J-unitary group and the indefinite spectral data.
- *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* (`articles_maths/the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.md`), for the two families, their parities, the composition laws and the failure of the monoid.
- *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the sandwich by the indefinite adjoint, its laws, the form-preservation and the transport of kernel and image.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, the two actions of the unit and the absence of a unit.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the inertia and the restrictions of the form, and *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for $J$ and the anti-automorphism that drives the side swap.
- *The Krein Isometry Group and Its J-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`) and *The Indefinite Spectra of the Operators on the Biquaternion Algebra* (`articles_maths/the-indefinite-spectra-of-the-operators-on-the-biquaternion-algebra.md`), for the group $U(1,3)$ and the spectra.
- Companion articles of the band: *The Fourth Product and Its Indefinite Metric* (`articles_physics/the-fourth-product-and-its-indefinite-metric.md`), *The States the Indefinite Metric Cannot Normalise* (`articles_physics/the-states-the-indefinite-metric-cannot-normalise.md`) and *Why the Fourth Product Is a Gauge Structure and Not a State Space* (`articles_physics/why-the-fourth-product-is-a-gauge-structure-and-not-a-state-space.md`).
- *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich* (`articles_physics/the-operators-of-the-general-plain-bilinear-product-one-sided-two-sided-and-the-sandwich.md`), the composition-band sibling whose transpose swaps the sides, and *Observables, Gauge Generators and the Chirality of the Internal Action* (`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the definite Hermitian adjoint of the observables, and *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader of the twelve.
