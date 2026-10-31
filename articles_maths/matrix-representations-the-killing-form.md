# __Matrix Representations : The Killing Form__

## Introduction

The Killing form of the biquaternion algebra is one complex bilinear form $\kappa_{\mathbb{C}}$, independent of the display. The $2\times2$ model and the $4\times4$ regular model give two formulas for it,
$$
\kappa_{\mathbb{C}}=4\operatorname{tr}_2(XY)-2\operatorname{tr}_2X\operatorname{tr}_2Y
\qquad\text{and}\qquad
\kappa_{\mathbb{C}}=2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y,
$$
and the two formulas agree on corresponding elements because $\operatorname{tr}_4=2\operatorname{tr}_2$ and $\operatorname{tr}_4(XY)=2\operatorname{tr}_2(XY)$. The Peirce frame makes the agreement visible: the $4\times4$ formula is the $2\times2$ formula read twice.

The form is degenerate along the centre, which is its radical, and on the vector part it is $-8\vec X\cdot\vec Y$. This article develops the adjoint operator, the formula in the three displays, the radical, the signature, the invariance, the relation to the trace form and the Casimir.

**Conventions.** The algebra and the models are those of *Matrix Representations : The Models and the Change of Frame*. The bracket is $[X,Y]=XY-YX$, and $\kappa_{\mathbb{C}}$ is complex bilinear. The real Killing form is $\kappa=2\operatorname{Re}\kappa_{\mathbb{C}}$, twice the real part. The vector part carries $\vec X\cdot\vec Y=X_xY_x+X_yY_y+X_zY_z$, and $\operatorname{tr}_2$, $\operatorname{tr}_4$ are the complex traces of the two displays.

**Boundaries.** The Killing form of the algebra and its signature are *Biquaternion Lie Group and Exponential Structure*, §*The Killing Form*; the four forms are *Matrix Representations : The Four Words and the Four Traces*; the trace pairing is *Matrix Representations : Trace, Determinant and the Biquaternion Norm*; the operator-level adjoints are *The Four Adjoints of the Biquaternion Algebra in Examples*.

## The Adjoint Operator

**The definition.** For $X$ in the image,
$$
\operatorname{ad}_X(Y)=[X,Y].
$$
It is complex linear, a derivation, and it preserves the image:
$$
\operatorname{ad}_{\mathsf M_4^L(\tilde X)}\bigl(\mathsf M_4^L(\tilde Y)\bigr)
=\mathsf M_4^L\bigl([\tilde X,\tilde Y]\bigr).
$$
The adjoint of the regular model is therefore the image of the adjoint of the algebra, and the Killing form of the image is the Killing form of $\mathbb{B}$.

**The eigenvalues.** On the matrix units of a diagonal element, $\operatorname{ad}_X(E_{ij})=(x_i-x_j)E_{ij}$. The eigenvalues of $\operatorname{ad}_X$ are the differences of the eigenvalues of $X$, each repeated according to multiplicity. On the four-dimensional image every nonzero difference occurs once, which is why the intrinsic trace is the $2\times2$ trace; on the ambient $M_4(\mathbb{C})$ every difference occurs four times, which is why the ambient form is four times the intrinsic one.

**The ambient operator.** On the ambient $M_4(\mathbb{C})$ the operator $\operatorname{ad}_M$ also acts on the two off-diagonal blocks, because the ambient algebra is larger than the image. The ambient Killing form therefore differs from the intrinsic one by the contribution of the twelve transverse directions; the two forms are compared in §*The Ambient Restriction*.

## The Formula

**The invariant form.** The Killing form is
$$
\kappa_{\mathbb{C}}(X,Y)=\operatorname{tr}\bigl(\operatorname{ad}_X\operatorname{ad}_Y\bigr).
$$
The centre lies in the radical because $\operatorname{ad}_{\mathrm I}=0$. On the trace-free part the form is nondegenerate, and on the vector part it is proportional to the Euclidean form.

**The $2\times2$ display.** For $X=\mathsf M_2(\tilde X)$ and $Y=\mathsf M_2(\tilde Y)$,
$$
\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}_2(XY)-2\operatorname{tr}_2X\operatorname{tr}_2Y
$$
and on the vector part
$$
\kappa_{\mathbb{C}}(X,Y)=-8\,\vec X\cdot\vec Y.
$$

**The $4\times4$ display.** For $X=\mathsf M_4^L(\tilde X)$ and $Y=\mathsf M_4^L(\tilde Y)$,
$$
\kappa_{\mathbb{C}}(X,Y)=2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y
$$
and the coordinate form is the same,
$$
\kappa_{\mathbb{C}}(X,Y)=-8\,\vec X\cdot\vec Y.
$$

**The agreement.** In the Peirce frame $X=I_2\otimes B_1$ and $Y=I_2\otimes B_2$, so $\operatorname{tr}_4(XY)=2\operatorname{tr}_2(B_1B_2)$ and $\operatorname{tr}_4X=2\operatorname{tr}_2B_1$. Substituting,
$$
2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y
=4\operatorname{tr}_2(B_1B_2)-2\operatorname{tr}_2B_1\operatorname{tr}_2B_2.
$$
The $4\times4$ formula is the $2\times2$ formula read twice. The scalar $\kappa_{\mathbb{C}}$ is one number, and the two displays compute it in two ways.

**The proof of the coordinate form.** On the vector part $X=\vec X$, $Y=\vec Y$ and $\operatorname{tr}X=\operatorname{tr}Y=0$, so the formula reduces to $2\operatorname{tr}_4(XY)$ in the regular model and $4\operatorname{tr}_2(XY)$ in the $2\times2$ model. With $\vec X=\sum X_k\vec e_k$, the product $XY$ has scalar part $-\vec X\cdot\vec Y$ and vector part $\vec X\times\vec Y$; hence $\operatorname{tr}_4(XY)=-4\vec X\cdot\vec Y$ and $\operatorname{tr}_2(XY)=-2\vec X\cdot\vec Y$. Both formulas give $-8\vec X\cdot\vec Y$.

**The real form.** Twice the real part is
$$
\kappa(X,Y)=-16\operatorname{Re}(\vec X\cdot\vec Y)
=4\operatorname{Re}\operatorname{tr}_4(XY)-\operatorname{Re}\bigl(\operatorname{tr}_4X\operatorname{tr}_4Y\bigr).
$$
The factor two is the realification of the complex trace, not a feature of the display.

## The Ambient Restriction

**The ambient form.** The Killing form of $\mathfrak{gl}_4(\mathbb{C})$ is
$$
\kappa_{\mathfrak{gl}_4}(X,Y)=8\operatorname{tr}_4(XY)-2\operatorname{tr}_4X\operatorname{tr}_4Y.
$$
On the image it equals
$$
\kappa_{\mathfrak{gl}_4}(X,Y)=4\kappa_{\mathbb{C}}(X,Y)=-32\,\vec X\cdot\vec Y.
$$
The factor four is the contribution of the twelve transverse directions: the ambient algebra has complex dimension sixteen, the image has dimension four, and the transverse part contributes three times the intrinsic trace.

**The intrinsic form.** The intrinsic Killing form is the one computed inside the image. The image is not an ideal of $M_4(\mathbb{C})$, so the ambient restriction is not the intrinsic form; the two differ by the factor four on the vector part and by the treatment of the centre. This article uses the intrinsic form unless the ambient one is named.

## The Radical

**The theorem.** The radical of $\kappa_{\mathbb{C}}$ is the centre:
$$
\operatorname{rad}\kappa_{\mathbb{C}}=\mathbb{C}\mathrm I_4
=\mathbb{C}\mathrm I_2,
\qquad
\operatorname{rad}\kappa=\mathbb{R}\mathrm I\oplus i\mathbb{R}\mathrm I,
$$
of complex dimension one and real dimension two.

*Proof.* The coordinate form depends only on the vector parts, so every scalar matrix is in the radical. Conversely, if $\kappa(X,Y)=0$ for all $Y$, then $\vec X=0$, because the Euclidean form is nondegenerate on the vector part; hence $X$ is scalar.

**The rank.** The complex form has rank three; the real form has rank six. The centre contributes two real radical directions, and the vector part contributes the remaining six real dimensions.

**The degeneration.** The algebra is reductive and not semisimple: it is the direct sum of the centre and $\mathfrak{sl}_2(\mathbb{C})$. The Killing form is zero on the first summand and nondegenerate on the second. The degeneration is exactly the centre, and it is the same in the two displays.

## The Signature

**The real vector part.** Write $X_k=p_k+ip'_k$ for the three vector coordinates. Then
$$
\operatorname{Re}(\vec X\cdot\vec X)=\sum_{k=1}^{3}\bigl(p_k^2-(p'_k)^2\bigr),
$$
a real quadratic form of signature $(3,3)$ on the six real dimensions of the vector part. The real Killing form is $-16$ times it, so its signature on the trace-free part is $(3,3)$.

**The compact real form.** On the real quaternion subspace, $p'_k=0$, and the form is $-16\sum p_k^2$, negative definite of signature $(0,3)$ on the vector part. This is the compact case: the Killing form of $\mathfrak{su}(2)$ is negative definite.

**The split real form.** On the split real form the vector part has signature $(2,1)$ under the dot product, and the Killing form has signature $(2,1)$ up to sign. The two real forms are the two real slices of the same complex form.

**The full real algebra.** The real algebra has real dimension eight: the centre contributes two radical directions, and the vector part contributes the signature $(3,3)$. The full signature is $(3,3)$ plus two zeros.

## Invariance

**The theorem.** For all $X,Y,Z$ in the image,
$$
\kappa([X,Y],Z)+\kappa(Y,[X,Z])=0.
$$

*Proof.* The adjoint representation is a Lie homomorphism, and the trace of a commutator vanishes:
$$
\kappa([X,Y],Z)
=\operatorname{tr}\bigl([\operatorname{ad}_X,\operatorname{ad}_Y]\operatorname{ad}_Z\bigr)
=-\operatorname{tr}\bigl(\operatorname{ad}_Y[\operatorname{ad}_X,\operatorname{ad}_Z]\bigr)
=-\kappa(Y,[X,Z]).
$$

**The consequence.** The form is invariant under the adjoint action, so it is a function of the conjugation class. It is also invariant under every algebra automorphism, because every automorphism of $\mathbb{B}$ is inner. The trace form $4\langle\tilde X,\tilde Y\rangle$ is invariant as well; the two forms differ by the centre and by a factor on the vector part.

## The Trace Form

**The trace pairing.** In the regular model,
$$
\operatorname{tr}_4(XY)=4\langle\tilde X,\tilde Y\rangle
=4\bigl(X_tY_t-\vec X\cdot\vec Y\bigr),
$$
of signature $(4,4)$ on the real algebra. In the $2\times2$ model the same formula is
$$
\operatorname{tr}_2(XY)=2\bigl(X_tY_t-\vec X\cdot\vec Y\bigr).
$$
The trace form is nondegenerate and its radical is zero; it sees the centre, which the Killing form does not.

**The comparison on the vector part.** There,
$$
\kappa_{\mathbb{C}}=-8\,\vec X\cdot\vec Y,
\qquad
\operatorname{tr}_4(XY)=-4\,\vec X\cdot\vec Y,
\qquad
\operatorname{tr}_2(XY)=-2\,\vec X\cdot\vec Y,
$$
so $\kappa_{\mathbb{C}}=2\operatorname{tr}_4(XY)=4\operatorname{tr}_2(XY)$ on the vector part. On the centre the trace form is nondegenerate, of signature $(1,1)$ over the real centre, and the Killing form vanishes. The two forms therefore agree on $\mathfrak{sl}_2$ up to the factor two of the regular trace, and differ completely on the centre.

**The table.**

| Property | Trace form $\operatorname{tr}(XY)$ | Killing form $\kappa$ |
|---|---|---|
| Nondegenerate on the image | yes | no; radical the centre |
| Nondegenerate on $\mathfrak{sl}_2$ | yes | yes |
| Signature on $\mathfrak{sl}_2$ | $(3,3)$ | $(3,3)$ |
| Vanishes on the centre | no | yes |
| Invariant under all automorphisms | yes | yes |

The trace form is the trace of the defining representation; the Killing form is the trace of the adjoint representation. The difference is the centre.

## The Casimir

**The vector Casimir.** On the vector subspace, with $\kappa_{\mathbb{C}}=-8\vec X\cdot\vec Y$, the dual of $\vec e_k$ is $-\vec e_k/8$, and the Casimir is
$$
\Omega=-\frac18\sum_{k=1}^{3}\mathsf M_4^L(\vec e_k)^2.
$$
Since $\mathsf M_4^L(\vec e_k)^2=-\mathrm I_4$ for each $k$, the Casimir is
$$
\Omega=\frac38\mathrm I_4.
$$
The same scalar $\tfrac38$ acts on each copy of the defining module, and in the $2\times2$ display the Casimir is $\tfrac38\mathrm I_2$. The value is the same because the vector part has three dimensions in both displays and the normalization of $\kappa_{\mathbb{C}}$ is the same.

**The scalar action.** The Casimir acts on the defining module by the scalar $\tfrac38$, not by a nontrivial matrix. The reason is that the vector part acts irreducibly on each spinor plane, and Schur's lemma forces the invariant to be scalar. In the regular model the module is the direct sum of two copies, and the Casimir is the scalar on both.

## Summary

The Killing form is one complex bilinear form, $\kappa_{\mathbb{C}}=4\operatorname{tr}_2(XY)-2\operatorname{tr}_2X\operatorname{tr}_2Y=2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y=-8\vec X\cdot\vec Y$. Its real form is $\kappa=-16\operatorname{Re}(\vec X\cdot\vec Y)$, of signature $(3,3)$ on the trace-free part. Its radical is the centre, of complex dimension one and real dimension two. The form is invariant under the adjoint action and under every automorphism, it differs from the nondegenerate trace form by the centre and by the factor two of the regular trace, and its Casimir on the vector subspace is $\tfrac38$ times the identity in both displays.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\kappa_{\mathbb{C}}=4\operatorname{tr}_2(XY)-2\operatorname{tr}_2X\operatorname{tr}_2Y$ | the complex form in the $2\times2$ display |
| $\kappa_{\mathbb{C}}=2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y$ | the complex form in the $4\times4$ display |
| $\kappa=-16\operatorname{Re}(\vec X\cdot\vec Y)$ | the real form |
| $\operatorname{rad}\kappa=\mathbb{C}\mathrm I$ | the centre |
| $(3,3)$ | the signature on the trace-free part |
| $\Omega=\tfrac38\mathrm I$ | the Casimir on the vector subspace |
| $\kappa_{\mathfrak{gl}_4}=4\kappa_{\mathbb{C}}$ | the ambient restriction on the image |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the models and the traces
- [Matrix Representations : The Four Words and the Four Traces](matrix-representations-the-four-words-and-the-four-traces.html), for the trace pairing
- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the trace and the norm
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Lie algebra and the Killing form
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms
- [$M_2(\mathbb{C})$ Representation : The Killing Form](m2c-representation-the-killing-form.html), for the $2\times2$ source
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Killing Form](m4c-representation-the-killing-form.html), for the $4\times4$ source
