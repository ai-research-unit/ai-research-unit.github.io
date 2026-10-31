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

## Common Aspects

The Killing form of the biquaternion algebra is one complex bilinear form $\kappa_{\mathbb{C}}$, independent of the display. It is degenerate along the centre, which is its radical, and on the vector part it is $-8\vec X\cdot\vec Y$. The $2\times2$ and $4\times4$ formulas are two ways of computing the same number, and they agree because the regular trace is twice the entry trace.

**The invariant form.** The Killing form is
$$
\kappa_{\mathbb{C}}(X,Y)=\operatorname{tr}\bigl(\operatorname{ad}_X\operatorname{ad}_Y\bigr),
\qquad
\operatorname{ad}_X(Y)=[X,Y].
$$
The adjoint is complex linear, a derivation, and preserves the image: $\operatorname{ad}_{\mathsf M_4^L(\tilde X)}(\mathsf M_4^L(\tilde Y))=\mathsf M_4^L([\tilde X,\tilde Y])$. On the matrix units of a diagonal element, $\operatorname{ad}_X(E_{ij})=(x_i-x_j)E_{ij}$, so the eigenvalues of $\operatorname{ad}_X$ are the differences of the eigenvalues of $X$, repeated according to multiplicity. On the four-dimensional image every nonzero difference occurs once; on the ambient $M_4(\mathbb{C})$ every difference occurs four times, which is why the ambient form is four times the intrinsic one.

**The radical.** The radical is the centre:
$$
\operatorname{rad}\kappa_{\mathbb{C}}=\mathbb{C}\mathrm I_4=\mathbb{C}\mathrm I_2,
\qquad
\operatorname{rad}\kappa=\mathbb{R}\mathrm I\oplus i\mathbb{R}\mathrm I,
$$
of complex dimension one and real dimension two. The coordinate form depends only on the vector parts, so every scalar matrix is in the radical; conversely, if $\kappa(X,Y)=0$ for all $Y$, then $\vec X=0$, because the Euclidean form is nondegenerate on the vector part. The complex form has rank three and the real form rank six. The algebra is reductive and not semisimple: it is the direct sum of the centre and $\mathfrak{sl}_2(\mathbb{C})$, the form is zero on the first summand and nondegenerate on the second.

**The signature.** Write $X_k=p_k+ip'_k$ for the three vector coordinates. Then
$$
\operatorname{Re}(\vec X\cdot\vec X)=\sum_{k=1}^{3}\bigl(p_k^2-(p'_k)^2\bigr),
$$
of signature $(3,3)$ on the six real dimensions of the vector part. The real Killing form is $-16$ times it, so its signature on the trace-free part is $(3,3)$. On the compact real quaternion subspace the form is negative definite, of signature $(0,3)$ on the vector part, the compact case of $\mathfrak{su}(2)$; on the split real form the vector part has signature $(2,1)$ up to sign. The full real algebra has signature $(3,3)$ plus the two radical directions of the centre.

**Invariance.** For all $X,Y,Z$ in the image,
$$
\kappa([X,Y],Z)+\kappa(Y,[X,Z])=0.
$$
The proof is the trace of a commutator: $\kappa([X,Y],Z)=\operatorname{tr}([\operatorname{ad}_X,\operatorname{ad}_Y]\operatorname{ad}_Z)=-\kappa(Y,[X,Z])$. The form is therefore invariant under the adjoint action and under every automorphism, because every automorphism of $\mathbb{B}$ is inner.

**The trace form.** The trace pairing is
$$
\operatorname{tr}_4(XY)=4\langle\tilde X,\tilde Y\rangle=4\bigl(X_tY_t-\vec X\cdot\vec Y\bigr)
$$
in the regular model and $\operatorname{tr}_2(XY)=2\langle\tilde X,\tilde Y\rangle$ in the entry model. It is nondegenerate, its radical is zero, and it sees the centre, which the Killing form does not. On the vector part $\kappa_{\mathbb{C}}=2\operatorname{tr}_4(XY)=4\operatorname{tr}_2(XY)$; on the centre the trace form is nondegenerate and the Killing form vanishes.

| Property | Trace form $\operatorname{tr}(XY)$ | Killing form $\kappa$ |
|---|---|---|
| Nondegenerate on the image | yes | no; radical the centre |
| Nondegenerate on $\mathfrak{sl}_2$ | yes | yes |
| Signature on $\mathfrak{sl}_2$ | $(3,3)$ | $(3,3)$ |
| Vanishes on the centre | no | yes |
| Invariant under all automorphisms | yes | yes |

**The Casimir.** On the vector subspace, with $\kappa_{\mathbb{C}}=-8\vec X\cdot\vec Y$, the dual of $\vec e_k$ is $-\vec e_k/8$, and
$$
\Omega=-\frac18\sum_{k=1}^{3}\mathsf M_4^L(\vec e_k)^2.
$$
Since $\mathsf M_4^L(\vec e_k)^2=-\mathrm I_4$ for each $k$, the Casimir is $\Omega=\tfrac38\mathrm I_4$. It acts on each copy of the defining module by the scalar $\tfrac38$, and in the entry model it is $\tfrac38\mathrm I_2$. The value is the same because the vector part has three dimensions in both displays and the normalization of $\kappa_{\mathbb{C}}$ is the same.

## The Coefficient Frame

**The formula.** For $X=\mathsf M_4^L(\tilde X)$ and $Y=\mathsf M_4^L(\tilde Y)$,
$$
\kappa_{\mathbb{C}}(X,Y)=2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y,
$$
and on the vector part
$$
\kappa_{\mathbb{C}}(X,Y)=-8\,\vec X\cdot\vec Y.
$$

**The proof of the coordinate form.** On the vector part $\operatorname{tr}X=\operatorname{tr}Y=0$, so the formula reduces to $2\operatorname{tr}_4(XY)$. With $\vec X=\sum X_k\vec e_k$, the product $XY$ has scalar part $-\vec X\cdot\vec Y$ and vector part $\vec X\times\vec Y$; hence $\operatorname{tr}_4(XY)=-4\vec X\cdot\vec Y$, and the formula gives $-8\vec X\cdot\vec Y$.

**The ambient restriction.** The Killing form of $\mathfrak{gl}_4(\mathbb{C})$ is
$$
\kappa_{\mathfrak{gl}_4}(X,Y)=8\operatorname{tr}_4(XY)-2\operatorname{tr}_4X\operatorname{tr}_4Y.
$$
On the image it equals $4\kappa_{\mathbb{C}}=-32\vec X\cdot\vec Y$. The factor four is the contribution of the twelve transverse directions: the ambient algebra has complex dimension sixteen, the image dimension four, and the transverse part contributes three times the intrinsic trace.

**The trace form and the Casimir.** The regular trace form is $\operatorname{tr}_4(XY)=4\langle\tilde X,\tilde Y\rangle$, of signature $(4,4)$ on the real algebra, and the Casimir is $\tfrac38\mathrm I_4$.

## The Entry Model

**The formula.** For $X=\mathsf M_2(\tilde X)$ and $Y=\mathsf M_2(\tilde Y)$,
$$
\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}_2(XY)-2\operatorname{tr}_2X\operatorname{tr}_2Y,
$$
and on the vector part $\kappa_{\mathbb{C}}=-8\vec X\cdot\vec Y$. On the vector part the formula reduces to $4\operatorname{tr}_2(XY)$; since $\operatorname{tr}_2(XY)=-2\vec X\cdot\vec Y$, the result is again $-8\vec X\cdot\vec Y$.

**The trace form.** The entry trace form is $\operatorname{tr}_2(XY)=2\langle\tilde X,\tilde Y\rangle$, of signature $(4,4)$ after realification, and it is nondegenerate. The Casimir is $\tfrac38\mathrm I_2$. The factor two between the two trace forms is the factor two between the two traces: $\operatorname{tr}_4=2\operatorname{tr}_2$.

## The Peirce Frame

**The agreement.** In the Peirce frame $X=\mathrm I_2\otimes B_1$ and $Y=\mathrm I_2\otimes B_2$, so
$$
\operatorname{tr}_4(XY)=2\operatorname{tr}_2(B_1B_2),
\qquad
\operatorname{tr}_4X=2\operatorname{tr}_2B_1.
$$
Substituting,
$$
2\operatorname{tr}_4(XY)-\tfrac12\operatorname{tr}_4X\operatorname{tr}_4Y
=4\operatorname{tr}_2(B_1B_2)-2\operatorname{tr}_2B_1\operatorname{tr}_2B_2.
$$
The $4\times4$ formula is the $2\times2$ formula read twice. The block display makes the agreement visible without a change of frame: each trace is doubled and each product trace is doubled, so the two doublings cancel.

**The Casimir and the module.** The Casimir is $\tfrac38\mathrm I_4=\mathrm I_2\otimes(\tfrac38\mathrm I_2)$. It acts by the same scalar on each of the two spinor planes. The vector part acts irreducibly on each plane, and Schur's lemma forces the invariant to be scalar; the regular module is the direct sum of two copies, and the Casimir is that scalar on both.

**The ambient form.** The ambient $\mathfrak{gl}_4$ form restricts to four times the intrinsic form, because the twelve transverse directions are invisible to the image. The intrinsic form is the one computed inside the image; the image is not an ideal of $M_4(\mathbb{C})$, so the ambient restriction is not the intrinsic form.

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