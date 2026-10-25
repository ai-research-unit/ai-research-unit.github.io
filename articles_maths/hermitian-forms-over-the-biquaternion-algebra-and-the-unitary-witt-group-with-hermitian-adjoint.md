# __Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ be the biquaternion algebra with the Hermitian conjugation ${}^{*}$, fixed space $\mathbb{M}_+$ and anti-fixed space $\mathbb{M}_-$. This article is the biquaternion instance of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the companion of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*: that article studies the operator $\tilde Q_1\mapsto \tilde Q_1\tilde Q_2\tilde Q_1^{*}$ on the algebra, this one studies the **forms** on which the congruence $H\mapsto S^{*}HS$ acts, that is, the objects the two-sided operators are made to transform.

The results are the classical ones of a positive involution, made explicit in the matrix model: a Hermitian form on the algebra is a Hermitian matrix, congruence is the dagger congruence, **the invariant is the inertia** (Sylvester's law), every form is congruent to its normal form $\mathrm{diag}(1_{n},-1_{m},0_{r})$, the automorphism group of the unit form is the unitary slice $U=\mathrm{U}(2)$, and the forms modulo the hyperbolic ones form the **unitary Witt group** $W\cong\mathbb{Z}$, the invariant being the signature. Four facts of the algebra enter and none is special: the algebra is simple, the involution is positive, the centre is $\mathbb{C}$, and the rank-one module over the algebra is $\mathbb{C}^{2}$ in the matrix model.

## Hermitian Forms on the Algebra

**Definition.** Let $M$ be a right $\mathbb{B}$-module and let $h:M\times M\to\mathbb{B}$ be sesquilinear, $h(\tilde Q_1\lambda+\tilde Q_2\mu,\tilde Q)=\bar{\lambda}h(\tilde Q_1,\tilde Q)+\bar{\mu}h(\tilde Q_2,\tilde Q)$ and $h(\tilde Q_1,\tilde Q_2\lambda)=h(\tilde Q_1,\tilde Q_2)\lambda$. The form is **Hermitian** if in addition

$$
h(\tilde Q_2,\tilde Q_1) = h(\tilde Q_1,\tilde Q_2)^{*}.
$$

The form is **non-degenerate** if $h(\tilde Q_1,\tilde Q_2)=0$ for all $\tilde Q_2$ implies $\tilde Q_1=0$, and **positive definite** if $h(\tilde Q_1,\tilde Q_1)\in\mathbb{M}_+$ for $\tilde Q_1\neq0$, that is, if its values are positive in the sense of the Hermitian cone (*Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*).

**Proposition (the forms of the rank-one module).** Let $M=\mathbb{B}$ with the right action of the algebra on itself. Every Hermitian form on $M$ is

$$
h_{H}(\tilde Q_1,\tilde Q_2) = \tilde Q_1^{*}H\,\tilde Q_2\qquad\text{with } H\in\mathbb{M}_+,
$$

and the map $H\mapsto h_{H}$ is an isomorphism of the Hermitian elements onto the Hermitian forms. In the matrix model $\mathsf{M}_2(H)$ is a Hermitian $2\times2$ matrix and $h_{H}(\tilde Q_1,\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)^{*}\mathsf{M}_2(H)\mathsf{M}_2(\tilde Q_2)$.

*Proof.* Sesquilinearity and the Hermitian symmetry give $h(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}h(e_{t},\tilde Q_2)=\tilde Q_1^{*}h(e_{t},e_{t})\tilde Q_2$, with $H=h(e_{t},e_{t})\in\mathbb{M}_+$ by the symmetry, and conversely every such $h_{H}$ is a Hermitian form.

**Example (the unit form).** $\langle\cdot,\cdot\rangle_{*}=e_{t}$ gives $h_{e_{t}}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}\tilde Q_2$, of scalar part $\mathrm{Sc}(\tilde Q_1^{*}\tilde Q_2)=\sum_{\mu}Q_{1,\mu}^{*}Q_{2,\mu}$: the **unit form**, positive definite, the form of the Hermitian structure of the algebra and the trace form of the dagger. Its matrix in the basis $e_{\mu}$ is the identity.

**Example (the norm form, and why it is not here).** The quaternion norm $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\sum_{\mu}Q_{1,\mu}^{2}$ is a quadratic form of the algebra but it is **not** Hermitian for the dagger: $\langle\cdot,\cdot\rangle_{\natural}$ is complex-valued, indefinite and isotropic on the null cone. It is a form of the general plain bilinear type, not a form of the dagger, and the two must not be placed in the same classification (*Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*).

## Congruence and the Automorphism Group

**Definition.** Two Hermitian forms $h_{H},h_{H'}$ on the rank-one module are **congruent** if there is an invertible $S\in\mathbb{B}^{\times}$ with

$$
H' = S^{*}H\,S .
$$

Congruence is an equivalence relation, and the map $H\mapsto S^{*}HS$ is precisely the **two-sided operator** $\Theta_{S}$ of *Two-Sided Operators on the General Plain Sesqualgebra* applied to the form matrix. The invariants of congruence are the invariants of the two-sided operators seen on the Hermitian elements.

**Definition.** The **automorphism group** of $h_{H}$ is $\mathrm{U}(H)=\{\,S\in\mathbb{B}^{\times} : S^{*}HS=H\,\}$. For the unit form,

$$
\mathrm{U}(e_{t}) = \{\,S : S^{*}S=e_{t}\,\} = U ,
$$

the **unitary slice**, of real dimension four, with determinant-one part $\mathrm{SU}(2)$ (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*).

**Proposition (the slice acts by automorphisms and by congruence-preserving maps).** For $S\in U$ the operator $\Theta_{S}$ is unitary, an algebra automorphism and, on the Hermitian elements, a congruence that preserves the unit form; more generally $\mathrm{U}(H)$ is a subgroup of $\mathbb{B}^{\times}$ conjugate to $\mathrm{U}(e_{t})$ by any $S$ with $S^{*}H S$ the normal form of $\langle\cdot,\cdot\rangle_{*}$.

*Proof.* The automorphism and unitarity statements are the theorems of the two-sided operators; for the last, if $T^{*}HT$ is the normal form of $\langle\cdot,\cdot\rangle_{*}$ then $\mathrm{U}(H)=T^{-1}\mathrm{U}(e_{t})T$ up to the null directions, since $S^{*}HS=H$ is equivalent to $(TST^{-1})^{*}(T^{*}HT)(TST^{-1})=T^{*}HT$.

**Remark.** The three groups must not be confused: $\mathrm{U}(e_{t})=\mathrm{U}(2)$ is the automorphism group of the **unit** form; the automorphism group of the **norm** form is the Lorentz-type group $\{|N|=1\}/\pm1=SO^{+}(1,3)$ up to phase; and the two are different because the two forms are different. This is the same contrast as in *Biquaternion Versors and the Orthogonal Group*.

## Sylvester's Law of Inertia

**Definition.** For $H\in\mathbb{M}_+$ the **inertia** is the triple $(n,m,r)$ of the numbers of positive, negative and zero eigenvalues of the matrix $\mathsf{M}_2(H)$, that is of the positive, negative and null dimensions of the form $h_{H}$.

**Theorem (Sylvester's law of inertia).** Congruence preserves the inertia:

$$\boxed{\; H' = S^{*}HS,\ S\in\mathbb{B}^{\times}\quad\Longrightarrow\quad \mathrm{inertia}(H')=\mathrm{inertia}(H) \;}.$$

Moreover every Hermitian $\langle\cdot,\cdot\rangle_{*}$ is congruent to the **normal form**

$$
H \sim \mathrm{diag}\bigl(1_{n},\,-1_{m},\,0_{r}\bigr),\qquad (n,m,r)=\mathrm{inertia}(H).
$$

*Proof.* In the matrix model, $\langle\cdot,\cdot\rangle_{*}$ is Hermitian, so there is a unitary $V$ with $V^{*}HV=\mathrm{diag}(\lambda_{1},\lambda_{2})$, $\lambda_{i}\in\mathbb{R}$; the scalings $1/\sqrt{|\lambda_{i}|}$ on the nonzero directions give the normal form, and $S^{*}HS$ is Hermitian with the same signature by the inertia theorem for Hermitian matrices. The statement was verified on random Hermitian pairs with random invertible $S$, and the normal form was constructed explicitly from the eigenbasis.

**Corollary (additivity and the rank).** The signature $\sigma(H)=n-m$ and the rank $n+m$ are additive under the orthogonal sum,

$$
\sigma(H\oplus H')=\sigma(H)+\sigma(H'),\qquad \mathrm{rank}(H\oplus H')=\mathrm{rank}(H)+\mathrm{rank}(H'),
$$

and the inertia of the orthogonal sum is the sum of the inertias.

## The Classification and the Unitary Witt Group

**Theorem (the classification on the rank-one module).** The congruence classes of the Hermitian forms on the rank-one module over $\mathbb{B}$ are exactly the inertias with $n+m+r=2$:

$$\boxed{\; (2,0,0),\quad(1,1,0),\quad(0,2,0),\quad(1,0,1),\quad(0,1,1),\quad(0,0,2) \;}.$$

*Proof.* The normal form is determined by its inertia and the inertia is invariant, so two forms with the same inertia are congruent and two with different inertias are not.

**Definition (the hyperbolic plane).** The form of inertia $(1,1,0)$,

$$
\mathrm{Hyp} = \mathrm{diag}(1,-1),
$$

is the **hyperbolic plane**; the forms of inertia $(p+k,q+k,r)$ that are orthogonal sums of a form with the hyperbolic plane are **hyperbolic**. A non-degenerate form with $n=m$ is hyperbolic.

**Definition (the unitary Witt group).** On the non-degenerate Hermitian forms, call two forms **Witt equivalent** if they become congruent after adding hyperbolic planes to each. The classes form the **unitary Witt group** $W(\mathbb{B},{}^{*})$ under the orthogonal sum, the inverse of a class being given by the negation of the form.

**Theorem (the Witt group of the biquaternion algebra is $\mathbb{Z}$).** The signature is a complete invariant of the Witt class, and

$$\boxed{\; W(\mathbb{B},{}^{*}) \;\cong\; \mathbb{Z},\qquad \text{generated by the class of the unit form } h_{e_{t}} \;}.$$

*Proof.* The signature is additive, vanishes on the hyperbolic plane and changes sign under the negation, so it descends to a group homomorphism $W\to\mathbb{Z}$. It is injective because a form with signature zero has $n=m$, hence is hyperbolic, hence is the zero class; and it is surjective because the class of the unit form has signature $2$, so its multiples realise every even integer, while the class of the form $\mathrm{diag}(1,-1,-1,-1)$ has signature $-2$ and realises the negative ones. In the rank-two module the same argument applies with the signature of a $4\times4$ Hermitian matrix.

**Remark (what the group is not).** Over the complex numbers the signature classification collapses, since scaling by $i$ exchanges the signs and there is only one class up to congruence: the interesting group is the one of the **real** involution, which is the one used here since $\mathbb{M}_+$ is a real form. The Witt group is therefore $\mathbb{Z}$ and not $\mathbb{Z}/2$, and the invariant is the full signature, not only the parity of the rank.

## $\varepsilon$-Hermitian Forms and the Signed Involution

**Definition.** Let $\theta$ be an involution of $\mathbb{B}$ and let $\varepsilon=\pm1$. A form is **$\varepsilon$-Hermitian** for $\theta$ if $h(\tilde Q_2,\tilde Q_1)=\varepsilon\,\theta(h(\tilde Q_1,\tilde Q_2))$. The case $\varepsilon=+1$ is the Hermitian case of the article; the case $\varepsilon=-1$ is the **skew-Hermitian** case, and for $\theta=\mathrm{id}$ the two cases are the symmetric and the alternating bilinear forms, whose classification over a field of characteristic not two is again by congruence but with the alternating forms contributing the hyperbolic class.

**Remark (the four combinations of the corpus).** The corpus's four two-sided operators are the four combinations of the left twist, identity or signed, and the right factor, inverse or dagger: $\Theta_{\tilde Q_1}$ for the twisted cases and $\mathrm{H}_{\tilde Q_1}$ for the Hermitian ones (*Mixed Inner Conjugation and Hermitian Adjoint*). Each of them acts on the forms of the corresponding type: the congruence $H\mapsto S^{*}HS$ is the Hermitian case, the congruence $H\mapsto S^{*}HS$ with the twist $\alpha$ is the signed case, and the two have the same inertia theory because the twist is an isomorphism of $\mathbb{M}_+$.

## Worked Examples

**The unit form and the norm form.** The unit form has inertia $(2,0,0)$ and signature $2$; the form $\mathrm{diag}(1,-1)$ has inertia $(1,1,0)$ and signature $0$ and is the hyperbolic plane; the form $\mathrm{diag}(1,0)$ has inertia $(1,0,1)$ and rank one. The norm form $\langle\cdot,\cdot\rangle_{\natural}$ is not in the classification at all.

**The congruence by a two-sided operator.** For $S=e_{t}+\vec e_x$, of determinant two and invertible, and $\langle\cdot,\cdot\rangle_{*}=\mathrm{diag}(1,-1)$, the congruent form $S^{*}HS$ has the same inertia $(1,1,0)$. For $S$ a null element, $\langle S,S\rangle_{\natural}=0$, $S$ is not invertible and the congruence is not an equivalence: the form $\mathrm{diag}(1,0)$ is reached, and the rank drops. This is the algebraic content of the collapse worked in *Two-Sided Operators on the General Plain Sesqualgebra*.

**The automorphism group of the unit form.** $\mathrm{U}(e_{t})=\mathrm{U}(2)$: the maps $S$ with $S^{*}S=e_{t}$, exactly the unitary slice, of real dimension four. The automorphism group of the hyperbolic plane $\mathrm{diag}(1,-1)$ is $\mathrm{U}(1,1)$, indefinite, of real dimension four as well: the two forms have automorphism groups of the same dimension though the groups themselves differ, which is the group-level shadow of the difference of the signatures.

**The Witt class of a sum.** $\mathrm{diag}(1,1)\oplus\mathrm{diag}(-1,-1)$ has signature zero, hence is hyperbolic, hence is the zero Witt class, even though each summand is non-degenerate: this is the collapse that the Witt group performs and the inertia does not.

## Summary

A Hermitian form on the rank-one module over the biquaternion algebra is a Hermitian matrix $\langle\cdot,\cdot\rangle_{*}$, $h_{H}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}H\tilde Q_2$; congruence $H\mapsto S^{*}HS$ is the two-sided operator of the corpus applied to the form, and its equivalence classes are the **inertias** $(n,m,r)$ with $n+m+r=2$, by **Sylvester's law**, with normal form $\mathrm{diag}(1_{n},-1_{m},0_{r})$. The signature $\sigma=n-m$ and the rank are additive under the orthogonal sum. The automorphism group of the unit form $h_{e_{t}}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}\tilde Q_2$ is the unitary slice $U=\mathrm{U}(2)$, and the group of the quaternion norm is a different group, because the two forms are of different types. The hyperbolic plane $\mathrm{diag}(1,-1)$ is the null form of the Witt theory, and the non-degenerate forms modulo the hyperbolic ones form the **unitary Witt group $W(\mathbb{B},{}^{*})\cong\mathbb{Z}$**, generated by the unit form and computed by the signature. The $\varepsilon$-Hermitian case is the signed analogue, with the same inertia theory because the twist is an isomorphism of the Hermitian cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h_{H}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}H\tilde Q_2$ | Hermitian form of the rank-one module, $H\in\mathbb{M}_+$ |
| $h_{e_{t}}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{*}\tilde Q_2$ | The unit form; positive definite; trace form of the dagger |
| $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\sum_{\mu}Q_{1,\mu}^{2}$ | The quaternion norm; **not** a Hermitian form of the dagger |
| $H'\sim H \iff H'=S^{*}HS$ | Congruence; the two-sided operator on the form matrix |
| $(n,m,r)$ | Inertia: positive, negative and null dimensions |
| $\mathrm{diag}(1_{n},-1_{m},0_{r})$ | Sylvester normal form |
| $\mathrm{Hyp}=\mathrm{diag}(1,-1)$ | The hyperbolic plane; signature $0$, Witt class $0$ |
| $\mathrm{U}(H)=\{S:S^{*}HS=H\}$ | Automorphism group; $\mathrm{U}(e_{t})=\mathrm{U}(2)$ |
| $\sigma=n-m$ | Signature; complete invariant of the Witt class |
| $W(\mathbb{B},{}^{*})\cong\mathbb{Z}$ | The unitary Witt group, generated by the unit form |

## Further Reading

- [Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint](hermitian-forms-over-an-involution-ring-and-the-unitary-witt-group-with-hermitian-adjoint.html), the general theory of which this is the biquaternion instance.
- [Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint](hermitian-forms-on-a-hermitian-algebra-with-hermitian-adjoint.html), for the forms of an anti-involution and the canonical Hermitian form.
- [The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint](the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.html), for the same objects in coordinates: the forms, positivity, the cone and the slice.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the Hermitian elements and the real form.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the congruence as an operator, its invariants and its degenerate cases.
- [Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-a-hermitian-algebra-with-hermitian-adjoint.html), for the positive cone in which the signature lives.
- [The Unitary Slice and the Compact Real Form with Hermitian Adjoint](the-unitary-slice-and-the-compact-real-form-with-hermitian-adjoint.html), for the automorphism group of the unit form.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm, its isotropy and the group of units.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the automorphism group of the norm and the contrast with the slice.
- [Mixed Inner Conjugation and Hermitian Adjoint](mixed-inner-conjugation-and-hermitian-adjoint.html), for the four two-sided operators and the signed congruence.
