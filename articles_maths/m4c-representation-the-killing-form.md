# __$M_4(\mathbb{C})$ Representation : The Killing Form__

## Introduction

The Killing form of the biquaternion algebra is the invariant bilinear form of its Lie algebra. In the regular model it is a complex bilinear form on a four-dimensional subspace of $M_4(\mathbb{C})$, degenerate along the centre and proportional to the Euclidean form on the vector part. Its real part has signature $(3,3)$ on the trace-free part.

This article develops the adjoint operator, the formula, the radical, the signature, the invariance and the relation to the trace form. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Killing Form*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The Lie algebra is $\mathbb{B}$ with the bracket $[X,Y]=XY-YX$, read over $\mathbb{C}$ and over $\mathbb{R}$. Write $X=\mathsf{M}_4^{L}(\tilde X)$, $Y=\mathsf{M}_4^{L}(\tilde Y)$, and $\vec X\cdot\vec Y=X_xY_x+X_yY_y+X_zY_z$. The complex trace is written $\operatorname{tr}$.

**Boundaries.** The Killing form of the algebra is *Biquaternion Lie Group and Exponential Structure*, §*The Killing Form*; the four forms are *$M_4(\mathbb{C})$ Representation : The Four Words and the Four Traces*; the trace pairing is *$M_4(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Killing Form*.

**Frame.** Unless a basis is named, matrices are written in the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, where $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display: $\mathsf M_{4,\mathrm{coef}}^{L}=S\,(I_2\otimes\mathsf M_2)\,S^{-1}$, with $S$ the change of *The Product, the Trace and the Determinant*.

## The Adjoint Operator

For $X\in M_4(\mathbb{C})$ the **adjoint operator** is
$$
\operatorname{ad}_X:M_4(\mathbb{C})\longrightarrow M_4(\mathbb{C}),
\qquad
\operatorname{ad}_X(Y)=[X,Y]=XY-YX.
$$
It is complex linear, hence real linear on the thirty-two real dimensions, and it is a derivation of the matrix algebra.

**The image.** For $X=\mathsf{M}_4^{L}(\tilde X)$, the adjoint preserves the image:
$$
\operatorname{ad}_X(\mathsf{M}_4^{L}(\tilde Y))=\mathsf{M}_4^{L}([\tilde X,\tilde Y]).
$$
Hence the adjoint of the regular model is the image of the adjoint of the algebra, and the Killing form of the image is the Killing form of $\mathbb{B}$.

**The matrix units.** In the eigenbasis of a diagonal element, $\operatorname{ad}_X(E_{ij})=(x_i-x_j)E_{ij}$, so the adjoint is diagonal with the differences of the eigenvalues. The eigenvalues of $\operatorname{ad}_X$ are the differences of the eigenvalues of $X$, each repeated according to the multiplicity.

## The Formula

**The complex form.**
$$
\boxed{\;\kappa_{\mathbb{C}}(X,Y)=\operatorname{tr}\bigl(\operatorname{ad}_X\operatorname{ad}_Y\bigr)
=2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y\;}
$$
on the regular image.

*Proof.* The centre lies in the radical, because $\operatorname{ad}_{\mathrm I_4}=0$. On the trace-free part, the complex Killing form of $\mathfrak{sl}_2(\mathbb{C})$ is $4\operatorname{tr}(XY)$ in the $2\times2$ model; the regular model doubles the trace, so the invariant form is $2\operatorname{tr}(XY)$ on the traceless part. For general $X=a\mathrm I_4+U$ and $Y=b\mathrm I_4+V$ with $U,V$ traceless, the centre contributes nothing, so
$$
\kappa_{\mathbb{C}}(X,Y)=2\operatorname{tr}(UV)
=2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y.
$$

**The coordinate form.**
$$
\kappa_{\mathbb{C}}(X,Y)=-8\,\vec X\cdot\vec Y.
$$
The Killing form is the negative of eight times the Euclidean form on the vector part, and it does not see the scalar part.

**The real form.** The real Killing form is twice the real part of the complex one:
$$
\kappa(X,Y)=2\operatorname{Re}\kappa_{\mathbb{C}}(X,Y)
=4\operatorname{Re}\operatorname{tr}(XY)-\operatorname{Re}\bigl(\operatorname{tr}X\operatorname{tr}Y\bigr)
=-16\operatorname{Re}(\vec X\cdot\vec Y).
$$
On the $2\times2$ model the analogous formulas are
$$
\kappa_{\mathbb{C}}=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y,
\qquad
\kappa=8\operatorname{Re}\operatorname{tr}(XY)-4\operatorname{Re}\bigl(\operatorname{tr}X\operatorname{tr}Y\bigr),
$$
with the same coordinate form $-8\vec X\cdot\vec Y$ and $-16\operatorname{Re}(\vec X\cdot\vec Y)$.

**The ambient restriction.** The image is not an ideal of $M_4(\mathbb{C})$, so the restriction of the ambient Killing form is not the intrinsic one. The ambient form of $\mathfrak{gl}_4(\mathbb{C})$ is
$$
\kappa_{\mathfrak{gl}_4}(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y
$$
in the complex normalization, and on the image it equals
$$
-32\,\vec X\cdot\vec Y=4\kappa_{\mathbb{C}}(X,Y).
$$
The factor four is the contribution of the twelve transverse directions.

## The Radical

**Theorem.** The radical of the Killing form is the centre:
$$
\operatorname{rad}\kappa_{\mathbb{C}}=\mathbb{C}\mathrm I_4,
\qquad
\operatorname{rad}\kappa=\mathbb{R}\mathrm I_4\oplus i\mathbb{R}\mathrm I_4.
$$

*Proof.* The coordinate form depends only on the vector parts, so every scalar matrix is in the radical. Conversely, if $\kappa(X,Y)=0$ for all $Y$, then $\vec X=0$, so $X$ is scalar.

**The rank.** The complex form has rank three; the real form has rank six. The centre contributes two real radical directions.

**The degeneracy is the centre.** The algebra is reductive, not semisimple: it is the direct sum of the centre and $\mathfrak{sl}_2(\mathbb{C})$, and the Killing form is nondegenerate on the second summand and zero on the first.

## The Trace-Free Part and the Signature

**The real vector part.** Write $X_k=p_k+ip'_k$. Then
$$
\operatorname{Re}(\vec X\cdot\vec X)=\sum_k(p_k^2-(p'_k)^2),
$$
a real quadratic form of signature $(3,3)$ on the six real dimensions of the vector part. The real Killing form is $-16$ times it, so its signature is $(3,3)$.

**The compact real form.** On the real quaternion subspace, $p'_k=0$, and the form is $-16\sum p_k^2$, negative definite of signature $(0,3)$ on the vector part. This is the compact case: the Killing form of $\mathfrak{su}(2)$ is negative definite.

**The split real form.** On the split real form the vector part has signature $(2,1)$ under the dot product, and the Killing form has signature $(2,1)$ up to sign. The two real forms are the two signatures of the same complex form.

**The full real algebra.** The real algebra has real dimension eight: the centre contributes two radical directions and the vector part contributes the signature $(3,3)$. The full signature is $(3,3)$ plus two zeros.

## The Real Forms and the Signature

**The compact form.** On the real quaternion subspace, the Killing form is negative definite on the vector part and zero on the centre. The Lie algebra is $\mathfrak{su}(2)\oplus\mathbb{R}$, and the group is $SU(2)\times\mathbb{R}_{>0}$ up to the quotient.

**The split form.** On the split real form, the vector part has signature $(2,1)$, and the Killing form is indefinite. The Lie algebra is $\mathfrak{sl}_2(\mathbb{R})\oplus\mathbb{R}$, and the group is $GL_2(\mathbb{R})$ up to the centre.

**The complex form.** The complex algebra is the complexification of either real form, and the complex Killing form is the complexification of either real form. The two real signatures are the two real slices of the same complex form.

## Invariance

**Theorem.** For all $X,Y,Z$,
$$
\kappa([X,Y],Z)+\kappa(Y,[X,Z])=0.
$$

*Proof.* The adjoint representation is a Lie homomorphism, and the trace of a commutator vanishes:
$$
\kappa([X,Y],Z)=\operatorname{tr}(\operatorname{ad}_{[X,Y]}\operatorname{ad}_Z)
=\operatorname{tr}([\operatorname{ad}_X,\operatorname{ad}_Y]\operatorname{ad}_Z)
=-\operatorname{tr}(\operatorname{ad}_Y[\operatorname{ad}_X,\operatorname{ad}_Z])
=-\kappa(Y,[X,Z]).
$$

**The consequence.** The form is invariant under the adjoint action of the group, and it defines a symmetric invariant bilinear form on the Lie algebra. The trace form $4\langle\tilde X,\tilde Y\rangle$ is also invariant; the two differ by the centre and by a factor.

## Relation to the Trace Form

**The trace form.** The trace pairing of the regular model is
$$
\operatorname{tr}(XY)=4\langle\tilde X,\tilde Y\rangle
=4(X_tY_t-\vec X\cdot\vec Y),
$$
of signature $(4,4)$ on the real algebra. It is nondegenerate, and its radical is zero.

**The two forms compared.** The Killing form is the trace form of the adjoint representation; the trace form is the trace form of the defining representation. On the vector part they are proportional,
$$
\kappa_{\mathbb{C}}=-8\,\vec X\cdot\vec Y,
\qquad
\operatorname{tr}(XY)\big|_{\mathrm{Vect}}=4\,\vec X\cdot\vec Y,
$$
with ratio $-2$; on the centre the trace form is positive and the Killing form vanishes. The trace form sees the centre, the Killing form does not.

**The Casimir.** On the vector subspace, with the complex form $\kappa_{\mathbb{C}}=-8\vec X\cdot\vec Y$, the dual of $\vec e_k$ is $-\vec e_k/8$, and the Casimir is
$$
\Omega=-\frac18\sum_{k=1}^{3}\mathsf{M}_4^{L}(\vec e_k)^2.
$$
Since $\mathsf{M}_4^{L}(\vec e_k)^2=-\mathrm I_4$, the Casimir is $\Omega=\tfrac38\mathrm I_4$, the same scalar $\tfrac38$ as in the $2\times2$ model, acting on each copy of the defining module.

## Summary

The complex Killing form of the regular image is $2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y=-8\vec X\cdot\vec Y$; the real form is $-16\operatorname{Re}(\vec X\cdot\vec Y)$, of signature $(3,3)$ on the trace-free part. The radical is the centre, of complex dimension one and real dimension two. The form is invariant and degenerate, and it differs from the nondegenerate trace form by the centre and by a factor. The compact real form is negative definite on the vector part; the split real form is indefinite.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\kappa_{\mathbb{C}}=2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y$ | the complex Killing form |
| $\kappa=-16\operatorname{Re}(\vec X\cdot\vec Y)$ | the real Killing form |
| $\operatorname{rad}\kappa=\mathbb{C}\mathrm I_4$ | the centre |
| $(3,3)$ | the signature on the trace-free part |
| $\Omega=\tfrac38\mathrm I_4$ | the Casimir on the vector subspace |

## Further Reading

- [$M_4(\mathbb{C})$ Representation : The Four Words and the Four Traces](m4c-representation-the-four-words-and-the-four-traces.html), for the trace pairing
- [$M_4(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m4c-representation-trace-determinant-and-the-biquaternion-norm.html), for the trace
- [$M_2(\mathbb{C})$ Representation : The Killing Form](m2c-representation-the-killing-form.html), for the $2\times2$ version
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Lie algebra
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms
