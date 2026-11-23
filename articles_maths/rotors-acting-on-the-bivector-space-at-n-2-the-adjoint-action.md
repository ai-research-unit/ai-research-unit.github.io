# __Rotors Acting on the Bivector Space at $n=2$: the Adjoint Action__

## Introduction

**The adjoint action $X\mapsto qXq^{-1}$ of a rotor preserves the trace and the determinant, it preserves the two halves exactly when the rotor is orthogonal, and on the antisymmetric line an orthogonal rotor acts by the sign of its determinant, so at order two the bivector line carries only a sign.**

The article defines the adjoint action, lists its invariants, splits the algebra as the trace line plus the traceless part, proves that the traceless part carries the quadratic form $\operatorname{tr}(X^{2})$ with inertia $(2,1)$ over $\mathbb{R}$ and negative definite over the imaginary form, computes the kernel as the two scalars, and treats the orthogonal rotor case where the two halves are preserved and the bivector line is fixed or reversed. It assumes *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*, *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form* and *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$*.

It follows the biquaternion account of *The Endomorphisms of the Biquaternion Algebra* for the same action read on the eight real coordinates.

## The Adjoint Action

**Definition.** For an invertible $q$ the **adjoint action** is $\operatorname{Ad}_{q}(X)=qXq^{-1}$.

**Proposition.** The adjoint action is an algebra automorphism of $M_2(\mathbb{C})$, and $\operatorname{Ad}_{q}\circ\operatorname{Ad}_{r}=\operatorname{Ad}_{qr}$.

**Proof.** $(qXq^{-1})(qYq^{-1})=qXYq^{-1}$ shows that products are preserved; the composition law is immediate from the definition.

**Corollary.** The adjoint action is a homomorphism from $\mathrm{GL}_2(\mathbb{C})$ into the group of automorphisms of the algebra.

**Proof.** The composition law is that of a group action, and every $\operatorname{Ad}_{q}$ is invertible with inverse $\operatorname{Ad}_{q^{-1}}$.

**Corollary.** Two matrices are conjugate exactly when they lie in the same orbit of the adjoint action.

**Proof.** Conjugacy is the definition of the orbit relation.

## The Invariants

**Theorem.** The adjoint action preserves the trace, the determinant and the spectrum, and every polynomial in the matrix is carried to the same polynomial in the image.

**Proof.** The trace is invariant by the cyclic property, $\operatorname{tr}(qXq^{-1})=\operatorname{tr}(Xq^{-1}q)=\operatorname{tr}X$; the determinant is multiplicative, $\det(qXq^{-1})=\det q\det X\det q^{-1}=\det X$; and a polynomial in $qXq^{-1}$ equals $q$ times the polynomial in $X$ times $q^{-1}$.

**Corollary.** The characteristic polynomial and the spectrum are invariants of the orbit, so the discriminant is one as well.

**Proof.** Both are functions of the trace and the determinant at order two.

**Corollary.** The rank and the nullity are preserved, and so is the property of being an idempotent, a nilpotent or a scalar.

**Proof.** These properties are read from the spectrum and from the polynomial identities, which are preserved.

## The Trace Line and the Traceless Part

**Proposition.** The adjoint action fixes the trace line pointwise and preserves the traceless part, so the decomposition $M_2(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_2$ is equivariant.

**Proof.** The scalars commute with everything, so $\operatorname{Ad}_{q}(cI)=cI$; and the traceless part is the kernel of the trace, which is preserved because the trace is.

**Corollary.** The adjoint action on the four complex dimensions reduces to an action on the three-dimensional traceless part.

**Proof.** The action on the trace line is trivial, and the traceless part is three-dimensional.

**Corollary.** The decomposition of the traceless part into the traceless symmetric plane and the antisymmetric line is preserved exactly by the orthogonal rotors.

**Proof.** Conjugation preserves the transpose classes when $q$ is orthogonal, because then $(qXq^{-1})^{\mathsf T}=qX^{\mathsf T}q^{-1}$; and for a general $q$ the conjugate of an antisymmetric matrix need not be antisymmetric.

## The Preserved Form on the Traceless Part

**Theorem.** On $\mathfrak{sl}_2$ the adjoint action preserves the quadratic form $\operatorname{tr}(X^{2})$.

**Proof.** $\operatorname{tr}((qXq^{-1})^{2})=\operatorname{tr}(qX^{2}q^{-1})=\operatorname{tr}(X^{2})$ by the invariance of the trace.

**Corollary.** Over $\mathbb{R}$ the form has inertia $(2,1)$ in the basis $\operatorname{diag}(1,-1)$, $\sigma_{1}$, $J$, whose Gram matrix is $\operatorname{diag}(2,2,-2)$.

**Proof.** The three matrices are traceless and pairwise orthogonal for the form, with the squares computed directly; the two symmetric directions have the value $2$ and the antisymmetric direction has $-2$.

**Corollary.** Over the imaginary form the same computation gives the negative definite form on $\mathfrak{su}(2)$, so the real form of the group is $\mathrm{SO}(2,1)$ in one case and $\mathrm{SO}(3)$ in the other.

**Proof.** The traceless anti-Hermitian matrices have $\operatorname{tr}(X^{2})=-\operatorname{tr}(Y^{2})$ for $X=iY$, which is negative definite; the real traceless matrices have the mixed inertia.

## The Kernel and the Image

**Proposition.** The kernel of the adjoint action on $\mathrm{GL}_2(\mathbb{C})$ is the scalars, and on $\mathrm{SL}_2(\mathbb{C})$ it is the pair $\{\pm I\}$.

**Proof.** $\operatorname{Ad}_{q}$ is the identity exactly when $q$ commutes with every matrix, which forces $q$ to be a scalar; among the scalars of determinant one only $\pm I$ remain.

**Corollary.** The adjoint action of $\mathrm{SL}_2(\mathbb{C})$ is faithful only up to sign, and the group $\mathrm{PSL}_2(\mathbb{C})$ acts faithfully.

**Proof.** The two scalars act identically, and the quotient by them is the projective group.

**Corollary.** The image inside the orthogonal group of the traceless part is $\mathrm{SO}(2,1)$ for the real form and $\mathrm{SO}(3)$ for the imaginary form, and in the second case the map is onto.

**Proof.** The action preserves the form and has the right dimension in each case, and the standard identification of the double cover of the rotation group gives the surjectivity in the definite case.

## The Orthogonal Case and the Two Halves

**Theorem.** For an orthogonal rotor $q$ the adjoint action preserves the antisymmetric line and the symmetric plane, and on the antisymmetric line it acts by $\det(q)$.

**Proof.** Orthogonality gives $q^{-1}=q^{\mathsf T}$, so the conjugate of $X$ has the transpose class of $X$; and since the antisymmetric line is one-dimensional, $qJq^{-1}$ is a scalar multiple of $J$, and comparing determinants gives the scalar $\det q$.

**Corollary.** A rotation fixes the bivector line pointwise, and a reflection reverses it.

**Proof.** The determinant is one for a rotation and minus one for a reflection.

**Corollary.** The rotor action on the symmetric plane is a rotation of that plane, and the angle is twice the angle of the rotor.

**Proof.** The action preserves the form $\operatorname{tr}(X^{2})$, which is positive definite on the symmetric plane, so it is a rotation there; the doubling of the angle is the statement of the double cover computed for the traceless Hermitian space.

## The Bivector Line as a Sign

**Proposition.** The antisymmetric line of the biquaternion description, spanned by $J$, carries only the sign of the rotor, so at order two the bivector space has no angular information.

**Proof.** The line is one-dimensional and the action on it is multiplication by $\det q$, which is a sign for an orthogonal rotor and a general nonzero scalar for a general one.

**Corollary.** The angular information of a rotor at order two is carried by the symmetric plane and by the scalar-free part, not by the bivector line.

**Proof.** The bivector line carries one sign, and the symmetric plane carries a full angle.

**Corollary.** In the biquaternion language the same statement is that the pure part of the biquaternion is four-dimensional and the rotor acts on it by orthogonal transformations, of which only one sign lands on the antisymmetric direction.

**Proof.** The pure part of the biquaternion algebra is the orthogonal complement of the unit, and its antisymmetric direction is the one-dimensional line whose transformation is a sign.

## Summary

The adjoint action $X\mapsto qXq^{-1}$ is an algebra automorphism preserving the trace, the determinant and the spectrum. It fixes the trace line and acts on the three-dimensional traceless part, preserving the quadratic form $\operatorname{tr}(X^{2})$, which has inertia $(2,1)$ over the real form and is negative definite over the imaginary form; the kernel is the scalars, and on $\mathrm{SL}_2(\mathbb{C})$ it is the pair $\{\pm I\}$.

For an orthogonal rotor the two halves are preserved and the antisymmetric line is multiplied by $\det q$: rotations fix it and reflections reverse it. The symmetric plane then carries a rotation by twice the rotor angle, and the bivector line carries only a sign.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Ad}_{q}$ | the map $X\mapsto qXq^{-1}$ |
| $\mathfrak{sl}_2$ | the traceless part |
| $J$ | the antisymmetric generator |
| $\operatorname{tr}(X^{2})$ | the invariant quadratic form |
| $\mathrm{PSL}_2(\mathbb{C})$ | the adjoint group |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for adjoint actions and their kernels.
- Richard S. Hamilton, *Harmonic Maps of Manifolds with Boundary* (Springer, 1975), for the low-dimensional identifications of orthogonal groups.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the double cover used in the angle statement.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the infinitesimal form of the action.
- [The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m2r.html), for the inertia computation on the two halves.
