# __The Anti-Hermitian Subspace under the Four Forms__

## Introduction

The anti-Hermitian subspace $\mathbb{M}_-$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Introduction to the Six Subspaces* in the Algebra group. It reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so four times.

The algebra carries four pairings of its elements — the **complex bilinear form** $\langle\cdot,\cdot\rangle$, the **quaternion bilinear form** $\langle\cdot,\cdot\rangle_{\natural}$, the **complex sesquilinear form** $\langle\cdot,\cdot\rangle_{*}$ and the **quaternion sesquilinear form** $\langle\cdot,\cdot\rangle_{\natural*}$ of *The Four Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The four are kept apart in four separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **anti-Hermitian subspace** is the anti-fixed space of Hermitian conjugation, equivalently the fixed space of the reversal $\flat$, $\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\}$. It is the set of elements with imaginary scalar part and real vector part.

It is $\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$, of real dimension $4$; it is not a subalgebra, and it is a Lie algebra for the commutator.

## The Restriction of the Complex Bilinear Form

**Theorem (the restriction of the complex bilinear form).** On $\mathbb{M}_-$ the complex bilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = -(q'_0)^2-q_1^2-q_2^2-q_3^2 ,
$$

of signature $(0,4)$.

**Proof.** On the subspace $\tilde{Q}^{*}=-\tilde{Q}$, so $Q_0=iq'_0$ and $Q_k=q_k$ with real coordinates; $\langle\tilde{Q},\tilde{Q}\rangle=Q_0^2-\sum_kQ_k^2=-(q'_0)^2-\sum_kq_k^2$, negative in every direction.

The restriction is negative definite of signature $(0,4)$, the exact negative of the complex sesquilinear restriction on the same subspace; the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ are exchanged by multiplication by $i$, which reverses the sign of the complex bilinear form.

**The null set.** The form is negative definite, so the origin is its only isotropic point.

**The isometry group.** The restriction is a real form of signature $(0,4)$, so its group of **real-linear** isometries on $\mathbb{M}_-$ is $O(0,4)$; inside the ambient group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{M}_-$ form the corresponding subgroup.

## The Restriction of the Quaternion Bilinear Form

**Theorem (the restriction of the quaternion bilinear form).** On $\mathbb{M}_-$ the quaternion bilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (q_1^2+q_2^2+q_3^2)-(q'_0)^2 ,
$$

a real form of signature $(3,1)$ on the 4 real dimensions of the subspace.

**Proof.** On the subspace $Q_0=iq'_0$ and $Q_k=q_k$, so $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=(q_1^2+q_2^2+q_3^2)-(q'_0)^2$, three positive and one negative direction.

The restriction is the negative of the complex sesquilinear restriction, of signature $(3,1)$ rather than $(1,3)$; the two sectors are exchanged by multiplication by $i$.

**The null set.** the cone $\sum_kq_k^2=(q'_0)^2$, of real dimension $3$, the zero divisors of the subspace, none of which is nilpotent.

**The isometry group.** The restriction is a real form of signature $(3,1)$, so its group of **real-linear** isometries on $\mathbb{M}_-$ is the orthogonal group $O(3,1)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{M}_-$ form the corresponding subgroup.

## The Restriction of the Complex Sesquilinear Form

**Theorem (the restriction of the complex sesquilinear form).** On $\mathbb{M}_-$ the complex sesquilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*} = (q'_0)^2+q_1^2+q_2^2+q_3^2 ,
$$

of signature $(4,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu|Q_\mu|^2=|iq'_0|^2+\sum_kq_k^2$.

The restriction is the Euclidean square on the four real coordinates, positive definite, exactly as on the Hermitian sector.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 4 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $\mathbb{M}_-$ is the compact orthogonal group $O(4)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle_{*}=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the complex sesquilinear form.

## The Restriction of the Quaternion Sesquilinear Form

**Theorem (the restriction of the quaternion sesquilinear form).** On $\mathbb{M}_-$ the quaternion sesquilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural*} = (q'_0)^2-q_1^2-q_2^2-q_3^2 ,
$$

of signature $(1,3)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^2=(q'_0)^2-\sum_kq_k^2$, the signs $\varepsilon_k=-1$ falling on the real vector directions.

The quaternion sesquilinear restriction is the negative of the quaternion bilinear restriction, of signature $(1,3)$ rather than $(3,1)$; the passage between them is again the sign vector $\varepsilon$.

**The null set.** the cone $(q'_0)^2=\sum_kq_k^2$, of real dimension $3$, the light cone of the Lorentzian form on the subspace.

**The isometry group.** The restriction is a real form of signature $(1,3)$, so its group of **real-linear** isometries on $\mathbb{M}_-$ is $O(1,3)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $\mathbb{M}_-$ form the corresponding subgroup.

## The Four Forms Compared

The four restrictions are collected in one table; each entry is a form on the same real vector space $\mathbb{M}_-$, and the signatures are those of the underlying real form.

| form | expression | restriction on $\mathbb{M}_-$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| complex bilinear | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}\tilde{Q})$ | $-(q'_0)^2-\sum_kq_k^2$ | $(0,4)$ | negative definite | $\{0\}$ | $O(0,4)$ |
| quaternion bilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $\sum_kq_k^2-(q'_0)^2$ | $(3,1)$ | indefinite (Lorentzian) | $\sum_kq_k^2=(q'_0)^2$ | $O(3,1)$ |
| complex sesquilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ | $(q'_0)^2+\sum_kq_k^2$ | $(4,0)$ | positive definite | $\{0\}$ | $O(4)$ |
| quaternion sesquilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q}^{*})$ | $(q'_0)^2-\sum_kq_k^2$ | $(1,3)$ | indefinite (Lorentzian) | $(q'_0)^2=\sum_kq_k^2$ | $O(1,3)$ |

The four restrictions are: the complex bilinear form, negative definite of signature $(0,4)$; the quaternion bilinear form and the quaternion sesquilinear form, both Lorentzian, of signatures $(3,1)$ and $(1,3)$ respectively and negatives of one another; and the complex sesquilinear form, positive definite of signature $(4,0)$. The subspace is the anti-fixed space of the dagger; the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ are exchanged by multiplication by $i$, which reverses the sign of every one of the four forms.
## Summary

On the anti-Hermitian subspace the four forms give: the complex bilinear form $-(q'_0)^2-\sum_kq_k^2$ of signature $(0,4)$, negative definite; the quaternion bilinear form $\sum_kq_k^2-(q'_0)^2$ of signature $(3,1)$, with the cone $\sum_kq_k^2=(q'_0)^2$ as null set; the complex sesquilinear form $(q'_0)^2+\sum_kq_k^2$ of signature $(4,0)$, positive definite, the negative of the complex bilinear form; and the quaternion sesquilinear form $(q'_0)^2-\sum_kq_k^2$ of signature $(1,3)$, the negative of the quaternion bilinear form. The isometry groups are $O(0,4)$, $O(3,1)$, $O(4)$ and $O(1,3)$.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_-$ | the anti-Hermitian subspace, of real dimension $4$ |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the complex bilinear, quaternion bilinear, complex sesquilinear and quaternion sesquilinear forms of *The Four Pairings of the Biquaternion Algebra* |
| $(0,4)$ | the signature of the complex bilinear form on $\mathbb{M}_-$, negative definite
| $(3,1)$ | the signature of the quaternion bilinear form on $\mathbb{M}_-$, indefinite (Lorentzian)
| $(4,0)$ | the signature of the complex sesquilinear form on $\mathbb{M}_-$, the negative of the complex bilinear form
| $(1,3)$ | the signature of the quaternion sesquilinear form on $\mathbb{M}_-$, indefinite (Lorentzian)
| $O(0,4)$, $O(3,1)$, $O(4)$, $O(1,3)$ | the isometry groups of the four restrictions |
## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspace itself in the Algebra group
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms and the four Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the quaternion bilinear pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the complex sesquilinear pairing and the Euclidean norm it defines
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the complex bilinear pairing and its isotropic structure
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the quaternion sesquilinear pairing and the same six restrictions
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the six subspaces together and their intersections
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the operators attached to the third topology
