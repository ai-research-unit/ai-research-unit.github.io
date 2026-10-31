# __Matrix Representations : The Hermitian Sandwich__

## Introduction

The Hermitian sandwich is the map $X\mapsto\tilde QX\tilde Q^{*}$. It is the two-sided operator whose two parameters are conjugate, and it is the member of the two-sided family that carries the Lorentz action, the unitary slice and the positivity of the algebra. Its matrix is a Kronecker product of the $2\times2$ matrix of the element with its complex conjugate.

This article develops the operator and its laws, the two halves and the finer subspaces, the Peirce display, the coefficient display with the Lorentz matrix, and the unitary slice. It is the fourth of the articles on the operator families; the general two-sided family is *Matrix Representations : The Two-Sided Operators*.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$, with $B=\mathsf M_2(\tilde Q)$ and $\det B=\langle\tilde Q\rangle_{\natural}$. The Hermitian adjoint is
$$
\tilde Q^{*}=\overline{Q_t}e_t-\overline{Q_x}\vec e_x-\overline{Q_y}\vec e_y-\overline{Q_z}\vec e_z,
$$
and in the $2\times2$ model it is the conjugate transpose, $B(\tilde Q^{*})=B^{\dagger}$. The Peirce frame is $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, and the coefficient frame is $\mathcal B=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Boundaries.** The operator and its multiplicativity are *The Hermitian Sandwich : Definition and Multiplicativity*; the algebra instance is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*; the six subspaces are *Matrix Representations : The Six Subspaces as Matrix Conditions*; the two-sided family is *Matrix Representations : The Two-Sided Operators*; the unitary slice and the compact real form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the Lorentz action is *Biquaternion Rotations and Lorentz Transformations*.

## The Operator and Its Laws

**The definition.**
$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}.
$$
It is complex-linear in $X$ and depends on $\tilde Q$ through the pair $(\tilde Q,\tilde Q^{*})$.

**The composition law.**
$$
\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P},
$$
because $\tilde Q(\tilde PX\tilde P^{*})\tilde Q^{*}=(\tilde Q\tilde P)X(\tilde Q\tilde P)^{*}$. The family is therefore a representation of the multiplicative monoid, and $\Theta_{e_t}=\mathrm{id}$.

**The central rule.**
$$
\Theta_{z\tilde Q}=|z|^2\,\Theta_{\tilde Q},
\qquad z\in\mathbb{C}.
$$
The modulus, not the square, is the factor: the parameter enters once through $\tilde Q$ and once through its conjugate. The phase of $\tilde Q$ cancels, and the parameter is defined modulo the central circle $U(1)$.

**The defect from an automorphism.**
$$
\Theta_{\tilde Q}(X)\Theta_{\tilde Q}(Y)
=\tilde QX\,(\tilde Q^{*}\tilde Q)\,Y\tilde Q^{*}
=\Theta_{\tilde Q}\bigl(X\,(\tilde Q^{*}\tilde Q)\,Y\bigr).
$$
The product of the images is the image of the product with the defect $\tilde Q^{*}\tilde Q$ inserted between the factors. Hence $\Theta_{\tilde Q}$ is an algebra automorphism exactly when
$$
\tilde Q^{*}\tilde Q=e_t,
$$
that is, exactly on the $*$-unitary slice. The defect vanishes on the unit-norm part of the slice, not on the central dilations.

**The norm scaling.**
$$
\langle\Theta_{\tilde Q}(X)\rangle_{\natural}
=\langle\tilde Q\rangle_{\natural}\langle X\rangle_{\natural}\langle\tilde Q^{*}\rangle_{\natural}
=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle X\rangle_{\natural}.
$$
The sandwich therefore preserves the null cone $\langle X\rangle_{\natural}=0$ and the sign of the norm, and it sees only the modulus of the norm of the parameter.

**The invariants of the matrix.** With $M=\Theta_{\tilde Q}$,
$$
\operatorname{Tr}M=4\lvert Q_t\rvert^{2},
\qquad
\det M=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{4},
\qquad
\operatorname{rank}M=\operatorname{rank}(B)^{2}\in\{4,1,0\}.
$$
The rank is the square of the $2\times2$ rank, so a nonzero zero divisor gives a rank-one sandwich; there is no rank-two sandwich.

**The spectrum.** If $\lambda_+,\lambda_-$ are the eigenvalues of $B$, the eigenvalues of $M$ are the four products
$$
\lambda_+\overline{\lambda_+},\quad
\lambda_+\overline{\lambda_-},\quad
\lambda_-\overline{\lambda_+},\quad
\lambda_-\overline{\lambda_-},
$$
that is, $\lvert\lambda_+\rvert^{2}$, $\lambda_+\overline{\lambda_-}$, $\overline{\lambda_+}\lambda_-$ and $\lvert\lambda_-\rvert^{2}$.

## The Two Halves and the Finer Subspaces

**The two halves are always preserved.**
$$
X^{*}=X\ \Longrightarrow\ \Theta_{\tilde Q}(X)^{*}=\Theta_{\tilde Q}(X),
\qquad
X^{*}=-X\ \Longrightarrow\ \Theta_{\tilde Q}(X)^{*}=-\Theta_{\tilde Q}(X).
$$
The proof is one line: $(\tilde QX\tilde Q^{*})^{*}=\tilde QX^{*}\tilde Q^{*}$. The statement holds for every parameter, invertible or not.

**The centre is always preserved.** Since $\tilde Q\tilde Q^{*}=\sum_\mu\lvert Q_\mu\rvert^{2}e_t$ is a real scalar,
$$
\Theta_{\tilde Q}(\lambda e_t)=\lambda\Bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\Bigr)e_t .
$$
The centre is mapped into itself for every $\tilde Q$.

**The three finer subspaces.** The vector subspace $\mathrm{Vect}$, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ are preserved exactly when
$$
\tilde Q=z\tilde u,\qquad z\in\mathbb{C},\quad \tilde u^{*}=\tilde u^{-1},\quad \tilde u^{\natural}=\tilde u .
$$
For such a parameter, $\tilde Q^{*}=\bar z\,\tilde u^{-1}$ and
$$
\Theta_{\tilde Q}(X)=\lvert z\rvert^{2}\,\tilde uX\tilde u^{-1},
$$
a dilation composed with a real rotation. The vector subspace is preserved because the rotation is traceless-preserving; the two quaternion subspaces because $\tilde u$ is real. For a general parameter the defect $\tilde Q^{*}\tilde Q$ is not central, and the traceless part of a traceless matrix acquires a trace.

**The degenerate cases.** For $\tilde Q=0$ the sandwich is the zero map, which preserves every subspace but is not invertible. For a nonzero zero divisor the sandwich has rank one and cannot preserve the six subspaces, all of which have real dimension at least two.

**The two group readings.** The parameter set of the subspace-preserving maps is $\mathbb{C}^{\times}\times SO(3)$, of real dimension four; the parameter set of the automorphisms is the $*$-unitary group $U(2)$, of real dimension four; the two sets meet in $U(1)\times SO(3)$, where the scalars have modulus one. The automorphism group is not the whole subspace-preserving set, because a nontrivial dilation preserves the subspaces and is not an automorphism.

## The Peirce Display

**The matrix.** In the Peirce frame,
$$
\mathsf M(\Theta_{\tilde Q})
=\mathsf M_4^{L}(\tilde Q)\,\mathsf M_4^{R}(\tilde Q^{*})
=\bigl(B(\tilde Q^{*})^{\mathsf T}\otimes I_2\bigr)\bigl(I_2\otimes B\bigr)
=B(\tilde Q^{*})^{\mathsf T}\otimes B .
$$
Since $B(\tilde Q^{*})=B^{\dagger}$, the first factor is $\overline B$, and
$$
\boxed{\ \mathsf M(\Theta_{\tilde Q})=\overline B\otimes B\ }.
$$
The sandwich is the only member of the two-sided family whose two Kronecker factors are conjugate.

**The entries.** Writing $B=\begin{pmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{pmatrix}$,
$$
\overline B\otimes B=
\begin{pmatrix}
\overline{M_{11}}\,B&\overline{M_{12}}\,B\\[2pt]
\overline{M_{21}}\,B&\overline{M_{22}}\,B
\end{pmatrix},
$$
a block matrix whose four blocks are scalar multiples of the same $2\times2$ matrix $B$. This is the display in which the sandwich is visibly a two-sided operator of rank-one coefficient type.

**The trace and the determinant.**
$$
\operatorname{Tr}(\overline B\otimes B)=\operatorname{Tr}\overline B\cdot\operatorname{Tr}B=(2\overline{Q_t})(2Q_t)=4\lvert Q_t\rvert^{2},
$$
and
$$
\det(\overline B\otimes B)=(\det\overline B)^{2}(\det B)^{2}=\lvert N\rvert^{4}.
$$
The rank is $\operatorname{rank}\overline B\cdot\operatorname{rank}B=\operatorname{rank}(B)^{2}$.

**The spectrum.** The eigenvalues of $\overline B\otimes B$ are the products $\overline{\lambda_i}\lambda_j$; the four values are real on the diagonal pairs and conjugate on the off-diagonal pairs. The trace is their sum, $2\operatorname{Re}(\lambda_+\overline{\lambda_-})+2\lvert\lambda_+\rvert^{2}$ in the notation above, which equals $4\lvert Q_t\rvert^{2}$ because $\lambda_++\lambda_-=2Q_t$.

**The two halves in the block display.** A Hermitian $X$ has a Hermitian block coordinate in the Peirce frame, and the image under $\overline B\otimes B$ is again Hermitian by the general argument; the block display does not make the symmetry manifest, and the coefficient display does.

## The Coefficient Display and the Lorentz Matrix

**The matrix.** In the coefficient frame,
$$
\mathsf M_{\mathrm{coef}}(\Theta_{\tilde Q})
=\mathsf M^{L}_{\mathrm{coef}}(\tilde Q)\;\mathsf M^{R}_{\mathrm{coef}}(\tilde Q^{*})
=L(Q)\,D\,L(Q^{*})^{\mathsf T}D,
\qquad
D=\operatorname{diag}(1,-1,-1,-1).
$$
Equivalently, it is the two-sided coefficient matrix $c^{-1}\bigl([Q][Q^{*}]^{\mathsf T}\bigr)$ of *Matrix Representations : The Two-Sided Operators*, with coefficient matrix of rank one.

**The four-vector form.** On the anti-Hermitian half use the real basis
$$
(i e_t,\ e_x,\ e_y,\ e_z),
$$
in which a general anti-Hermitian element is $X=i x_0e_t+x_1e_x+x_2e_y+x_3e_z$ with real $x_\mu$. The form $-\langle X\rangle_{\natural}$ is
$$
-\langle X\rangle_{\natural}=x_0^{2}-x_1^{2}-x_2^{2}-x_3^{2},
$$
of signature $(1,3)$. The sandwich acts by a real $4\times4$ matrix,
$$
\mathsf M_{\mathrm{coef}}(\Theta_{\tilde Q})\,(i x_0,x_1,x_2,x_3)^{\mathsf T}
=\Lambda(\tilde Q)\,(i x_0,x_1,x_2,x_3)^{\mathsf T},
$$
where $\Lambda(\tilde Q)$ is the matrix whose columns are the coordinates of $\tilde Q(i e_\mu)\tilde Q^{*}$ in the same basis.

**The Lorentz theorem.**
$$
\Lambda(\tilde Q)^{\mathsf T}g\,\Lambda(\tilde Q)=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}g,
\qquad
g=\operatorname{diag}(1,-1,-1,-1).
$$
For $\langle\tilde Q\rangle_{\natural}=1$ the matrix lies in $SO^{+}(1,3)$; for a general unit the matrix is $\lvert N\rvert$ times a proper orthochronous Lorentz matrix.

*Proof.* The identity is the real form of the norm scaling $\langle\Theta_{\tilde Q}(X)\rangle_{\natural}=\lvert N\rvert^{2}\langle X\rangle_{\natural}$, read on the basis $(i e_t,e_x,e_y,e_z)$, where $-\langle\cdot\rangle_{\natural}$ is $g$. The determinant is $\lvert N\rvert^{4}$ and the time-time entry is
$$
\Lambda_{00}=\sum_\mu\lvert Q_\mu\rvert^{2}=\operatorname{Sc}(\tilde Q\tilde Q^{*})>0,
$$
so the matrix is future-pointing; its determinant is positive, so it is proper.

**The Hermitian half.** The same matrix acts on the Hermitian half in the real basis $(e_t,i e_x,i e_y,i e_z)$, where $\langle\cdot\rangle_{\natural}$ itself is $g$. The two halves carry the same Lorentz matrix, with the sign of the form reversed: this is the reason the table of the restructuring assigns the four-vector form to the anti-Hermitian half, where the physical metric is positive on the time direction.

**The null cone.** Since $\Lambda$ is a Lorentz similarity, it maps the cone $-\langle X\rangle_{\natural}=0$ to itself. On the anti-Hermitian half this is the light cone of the four-vector $x$; on the Hermitian half it is the same cone in the other real structure.

**The parameter count.** The map $\tilde Q\mapsto\Lambda(\tilde Q)$ is invariant under $\tilde Q\mapsto e^{i\theta}\tilde Q$, because the phase cancels between the two factors. The parameter space is therefore the unit group modulo $U(1)$, of real dimension $7$; on the norm-one slice it is $SL_2(\mathbb{C})/\{\pm1\}$, of real dimension six, and the cover
$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3)
$$
is twofold with kernel $\{\pm e_t\}$.

## The Unitary Slice

**The slice.** The $*$-unitary elements are those with $\tilde Q^{*}\tilde Q=e_t$. In the $2\times2$ model the dagger is the conjugate transpose, so the slice is
$$
U=\{\tilde Q:B^{\dagger}B=\mathrm I_2\}=U(2),
$$
of real dimension four. Its determinant-one part is $SU(2)\cong\mathrm{Spin}(3)$.

**The two slices are different.** The $*$-unitary slice $U(2)$ acts by automorphisms and is compact. The norm-one slice $\lvert\langle\tilde Q\rangle_{\natural}\rvert=1$ is $SL_2(\mathbb{C})$ up to phase, of real dimension six, and acts by Lorentz similarities. The first fixes the dagger; the second scales the quaternion norm by one. They meet in $SU(2)$ up to the central phase.

**The Lie algebra.** The tangent space at the identity is the space of $*$-anti-Hermitian elements, that is, $\mathfrak{u}(2)$; its traceless part is $\mathfrak{su}(2)$. The Cartan decomposition of the group of units is the decomposition of $\mathfrak{sl}_2(\mathbb{C})$ into $\mathfrak{su}(2)$ and the boosts, and the sandwich is the exponential of the adjoint action on that decomposition.

**The compact real form.** The positivity of the dagger, $\operatorname{Sc}(\tilde Q^{*}\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}>0$, is what makes the slice compact. It is the same positivity that makes the Hermitian cone of the algebra the cone of $M_2(\mathbb{C})$.

## Summary

The Hermitian sandwich $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ is the two-sided operator with conjugate parameters. It is multiplicative, $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$, with defect $\tilde Q^{*}\tilde Q$ and automorphism group the $*$-unitary slice $U(2)$. It preserves the Hermitian and anti-Hermitian halves and the centre for every parameter, and the vector and quaternion subspaces exactly for central multiples of real unit quaternions. Its norm scaling is $\lvert N\rvert^{2}$, so it preserves the null cone. In the Peirce frame its matrix is $\overline B\otimes B$, with trace $4\lvert Q_t\rvert^{2}$, determinant $\lvert N\rvert^{4}$ and rank $\operatorname{rank}(B)^{2}$. In the coefficient frame it acts on the anti-Hermitian half by the Lorentz matrix $\Lambda(\tilde Q)$, with $\Lambda^{\mathsf T}g\Lambda=\lvert N\rvert^{2}g$ and $\Lambda\in SO^{+}(1,3)$ on the norm-one slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the Hermitian sandwich |
| $\tilde Q^{*}$ | Hermitian adjoint, $B^{\dagger}$ in the $2\times2$ model |
| $\overline B\otimes B$ | the Peirce matrix |
| $4\lvert Q_t\rvert^{2}$ | the trace |
| $\lvert N\rvert^{4}$ | the determinant |
| $\operatorname{rank}(B)^{2}$ | the rank, in $\{4,1,0\}$ |
| $\lambda_i\overline{\lambda_j}$ | the four eigenvalues |
| $\Lambda(\tilde Q)$ | the Lorentz matrix on the anti-Hermitian half |
| $g=\operatorname{diag}(1,-1,-1,-1)$ | the Minkowski form |
| $U(2)$, $SU(2)$ | the $*$-unitary slice and its determinant-one part |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the coefficient sign matrix |

## Further Reading

- [Matrix Representations : The Two-Sided Operators](matrix-representations-the-two-sided-operators.html), for the general family
- [Matrix Representations : The Six Subspaces as Matrix Conditions](matrix-representations-the-six-subspaces-as-matrix-conditions.html), for the six subspaces
- [Matrix Representations : The Conjugations and the Adjoints](matrix-representations-the-conjugations-and-the-adjoints.html), for the dagger
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames
- [The Hermitian Sandwich : Definition and Multiplicativity](the-hermitian-sandwich-definition-and-multiplicativity.html), for the general theory
- [The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint](the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.html), for the algebra instance
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz action
