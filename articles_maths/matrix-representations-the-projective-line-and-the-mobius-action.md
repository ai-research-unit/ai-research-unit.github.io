# __Matrix Representations : The Projective Line and the Möbius Action__

## Introduction

The minimal one-sided ideals of the biquaternion algebra are parametrised by the projective line. In the entry model the ideal attached to a line $L$ is the set of matrices whose image lies in $L$; in the regular model it is the set of doubled matrices whose image lies in $L\oplus L$. The group of units acts by left multiplication, and in a chart the action is the Möbius transformation.

This article develops the ideals, the action and its kernel, the chart and the Möbius formula, the idempotents, the orbits and the cross-ratio, the Plücker form, and the real structure. It is the article in which the projective geometry of the algebra becomes the geometry of $\mathbb{P}^1(\mathbb{C})$.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. A vector of $\mathbb{C}^2$ is a column $\xi$, a line is written $[\xi]$, and the projective line is $\mathbb{P}^1(\mathbb{C})$. The chart is $z=\xi_1/\xi_2$ on the open set $\xi_2\neq0$, with $L_0=\operatorname{span}\{e_2\}$ at $z=0$ and $L_\infty=\operatorname{span}\{e_1\}$ at $z=\infty$. The entry matrix is $B=\mathsf M_2(\tilde Q)$ and the $4\times4$ regular matrix is $L=I_2\otimes B$. The Peirce frame is $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$.

**Boundaries.** The lattice of ideals and the parametrisation are *The Category of Modules*, §*The Projective Line and the Möbius Action*; the automorphism group is *Biquaternion Automorphisms and Derivations*; the real structure is *Matrix Representations : The Conjugations and the Adjoints*; the matrix statements are *Matrix Representations : The Projective Line and the Möbius Action*.

## Common Aspects

### The Action

**The definition.** For $M$ in the group of units and a line $L$,
$$
M\cdot L=ML,
\qquad
M\cdot I_L=I_{ML}.
$$
The product is a line, and the assignment is an action:
$$
M_1\cdot(M_2\cdot L)=(M_1M_2)\cdot L .
$$

**The kernel.** If $M$ acts trivially on every line, every vector is an eigenvector of $M$. A matrix with that property is scalar, so
$$
\ker=\mathbb{C}^{\times}\mathrm I,
\qquad
GL_2(\mathbb{C})/\mathbb{C}^{\times}\mathrm I_2\cong PGL_2(\mathbb{C}).
$$
The action factors through $PGL_2(\mathbb{C})$, the automorphism group of the algebra.

**The idempotent form.** On projectors the action is conjugation:
$$
\Pi\longmapsto M\Pi M^{-1},
$$
because $MI_{\operatorname{im}\Pi}=I_{M\operatorname{im}\Pi}=I_{\operatorname{im}(M\Pi M^{-1})}$.

### Orbits and the Cross-Ratio

**Transitivity.** The action is transitive: any two lines are carried to one another by an invertible matrix. The stabiliser of $z=0$ is the set of matrices with $b=0$,
$$
\left\{\begin{pmatrix}a&0\\c&d\end{pmatrix}:ad\neq0\right\},
$$
a Borel subgroup of $PGL_2(\mathbb{C})$, of complex dimension two.

**Triple transitivity.** The action is simply transitive on ordered triples of distinct points. A matrix is determined up to scalar by the images of three lines, and any three distinct lines can be sent to any other three.

**The cross-ratio.** For four distinct points,
$$
[z_1,z_2;z_3,z_4]=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}
$$
is invariant under every Möbius transformation, and it is the complete invariant of a quadruple: two quadruples are equivalent under $PGL_2(\mathbb{C})$ exactly when their cross-ratios agree.

**The meaning for the ideals.** The cross-ratio of four minimal ideals is the invariant of their configuration, and triple transitivity says that any ordered triple of distinct minimal ideals can be normalised to $(0,1,\infty)$ by a unique automorphism of the algebra.

### The Plücker Form

**The bracket.** For two vectors $\xi,\eta\in\mathbb{C}^2$,
$$
[\xi,\eta]=\det(\xi,\eta)=\xi_1\eta_2-\xi_2\eta_1 .
$$
The bracket is alternating and bilinear, and $[\xi,\eta]\neq0$ exactly when the two lines are distinct.

**The cross-ratio.**
$$
[\xi_1,\xi_2;\xi_3,\xi_4]
=\frac{[\xi_1,\xi_3]\,[\xi_2,\xi_4]}
{[\xi_1,\xi_4]\,[\xi_2,\xi_3]} .
$$
In the chart $\xi_i=(z_i,1)^{\mathsf T}$ this is the formula above, because $[\xi_i,\xi_j]=z_i-z_j$.

**Invariance.** Under $M\in GL_2(\mathbb{C})$,
$$
[M\xi,M\eta]=\det(M)\,[\xi,\eta],
$$
so every bracket in the numerator and the denominator is multiplied by the same determinant, and the cross-ratio is unchanged. This is the matrix reason for the invariance, and it defines the cross-ratio without a chart.

**Normalisation.** Three distinct lines can be sent to the three coordinate points, and the remaining freedom is the one complex parameter of the fourth line. In a basis $(\xi_1,\xi_2)$ with $\xi_3=\xi_1+\xi_2$ and $\xi_4=c\xi_1+d\xi_2$, the parameter is $c/d$, and it is the cross-ratio.

### The Real Structure

**Coefficient conjugation.** On matrices it acts by
$$
\sigma(M)=\epsilon\,\overline{M}\,\epsilon^{-1},
\qquad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
and on the defining module by the quaternionic structure $\xi\mapsto\epsilon\bar\xi$. On the chart,
$$
\xi=(z,1)^{\mathsf T}\longmapsto\epsilon\bar\xi=(1,-\bar z)^{\mathsf T},
\qquad
z\longmapsto-\frac{1}{\bar z}.
$$

**No fixed point.** The equation $z\bar z=-1$ has no complex solution, since $z\bar z=\lvert z\rvert^2\ge0$. Hence no minimal ideal is stable under coefficient conjugation. The real structure preserves the real projective line $\mathbb{P}^1(\mathbb{R})$ and acts on it as the antipodal map, with no fixed point.

**The intertwining.** Since $\sigma$ is antilinear,
$$
\sigma\circ\varphi_M=\varphi_{\sigma(M)}\circ\sigma .
$$
The two actions are paired by the real structure, and the orbit of a line is carried to the orbit of its conjugate.

**The compact picture.** The compact real form of $PGL_2(\mathbb{C})$ is $PU(2)\cong SO(3)$, and the projective line with its real structure is the two-sphere. The Möbius action restricts to the rotation action, and the cross-ratio restricts to the conformal invariant of four points on the sphere. The regular model carries two copies of the spinor space, and the two copies give the same Bloch vector.

## The Coefficient Frame

**The ideal as a plane.** In the coefficient frame the regular ideal is the conjugate of the doubled entry ideal,
$$
J_L^{\mathrm{coef}}=C_{\Pi}\bigl(I_2\otimes I_L\bigr)C_{\Pi}^{-1},
$$
a complex two-plane in $\mathbb{C}^4$. The two coordinate ideals are the images under $C_{\Pi}$ of the doubled Peirce ideals: $I_{L_\infty}$ is spanned by $I_2\otimes E_{11}$ and $I_2\otimes E_{21}$, and $I_{L_0}$ by $I_2\otimes E_{12}$ and $I_2\otimes E_{22}$.

**The action.** The group acts by left multiplication on the coefficient matrix,
$$
M\cdot J_L^{\mathrm{coef}}=(M_{\mathrm{coef}})\,J_L^{\mathrm{coef}}
=J_{ML}^{\mathrm{coef}},
$$
and the kernel is still the scalar matrices. The Möbius parameter is the line $L$ itself; the coefficient frame changes the plane that represents it, not the line.

**The invariant.** The projective line, the cross-ratio and the real structure are unchanged. The coefficient frame only writes the minimal ideal as a plane in the four-dimensional space, and the Plücker bracket of two lines is computed before the change, on the two spinor coordinates.

## The Entry Model

### The Ideals

**The entry model.** For a line $L\in\mathbb{P}^1(\mathbb{C})$ put
$$
I_L=\{M\in M_2(\mathbb{C}):\operatorname{im}M\subseteq L\}.
$$
Then $I_L$ is a minimal left ideal, and every minimal left ideal is $I_L$ for a unique $L$.

*Proof.* The set is a left ideal, because $\operatorname{im}(NM)\subseteq\operatorname{im}N\subseteq L$. In a basis with $L=\operatorname{span}\{e_1\}$ it is the space of matrices whose second column vanishes, of complex dimension two. A nonzero element has rank one and generates the whole ideal, so the ideal is minimal. Conversely, a minimal left ideal is generated by a rank-one idempotent $\Pi$, and it is $I_{\operatorname{im}\Pi}$; the image line is recovered as the common image of the nonzero elements.

**The two coordinate ideals.**
$$
I_{L_\infty}=\left\{\begin{pmatrix}a&0\\c&0\end{pmatrix}\right\}
=\mathbb{C}\{E_{11},E_{21}\},
\qquad
I_{L_0}=\left\{\begin{pmatrix}0&b\\0&d\end{pmatrix}\right\}
=\mathbb{C}\{E_{12},E_{22}\}.
$$
These are the two minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ of the Peirce decomposition.

### The Chart and the Möbius Formula

**The chart.** Write a line by the column $\xi=(z,1)^{\mathsf T}$, with $z=\xi_1/\xi_2$, and let
$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad ad-bc\neq0 .
$$
Then
$$
M\xi=\begin{pmatrix}az+b\\ cz+d\end{pmatrix},
\qquad
z'=\frac{az+b}{cz+d},
$$
which is the Möbius transformation attached to $M$. A nonzero scalar multiple of $M$ gives the same transformation, so the formula depends only on the class $[M]\in PGL_2(\mathbb{C})$, and composition is matrix multiplication:
$$
\varphi_{M_1}\circ\varphi_{M_2}=\varphi_{M_1M_2}.
$$

**The two coordinate points.** In this chart $I_{L_0}$ sits at $z=0$ and $I_{L_\infty}$ at $z=\infty$: the point at infinity is the line of the first basis vector. The two ideals are exchanged by $z\mapsto-1/z$, the image of
$$
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

### The Idempotents

**The fibre.** A rank-one idempotent is a nonzero matrix $\Pi$ with $\Pi^2=\Pi$ and rank one. Its image is a line $L$, its kernel is a line $K\neq L$, and it is the projection onto $L$ along $K$.

**The proposition.** Every rank-one idempotent with image $L$ and kernel $K$ is
$$
\Pi=u\eta,
$$
where $u$ spans $L$ and $\eta$ is the linear form with $\eta(u)=1$ and $\eta(K)=0$. The fibre of $\Pi\mapsto\operatorname{im}\Pi$ over $L$ is an affine line, parametrised by $K\neq L$.

*Proof.* The product satisfies $(u\eta)^2=u\eta(u)\eta=u\eta$, has image $L$ and kernel $\ker\eta=K$. Conversely a rank-one idempotent with image $L$ is determined by its kernel, and the formula recovers it. The kernels $K\neq L$ form $\mathbb{P}^1\setminus\{L\}$.

**The conjugacy class.** Every rank-one idempotent is conjugate to $E_{11}$, because $GL_2$ acts transitively on the pairs (image, kernel) and the stabiliser of $E_{11}$ is the diagonal torus, of complex dimension two. The class has complex dimension two and is the union of the affine fibres over the projective line of images.

**The four corners.** The idempotents $E_{11}$ and $E_{22}$ are orthogonal and sum to $\mathrm I_2$; they are the two coordinate points of the chart, and the Peirce decomposition is the decomposition into the four matrix units.

## The Peirce Frame

The regular model doubles the line and the ideals, and leaves the projective parameter unchanged.

### The Ideals

**The regular model.** For the same line put
$$
J_L=\{M\in\mathsf M_4^{L}(\mathbb{B}):\operatorname{im}M\subseteq L\oplus L\}.
$$
The set is a minimal right ideal of the regular image, and every minimal right ideal of the image is $J_L$ for a unique $L$. Its nonzero elements have rank two, and its complex dimension is two. The adjoint $J_L^{\dagger}$ is a minimal left ideal, and the two families are exchanged by the dagger.

**The rank.** In the entry model a minimal ideal consists of rank-one matrices; in the regular model it consists of rank-two matrices. The rank doubles with the size, and the parameter line does not.

### The Chart and the Möbius Formula

**The regular display.** The chart is the same, because the line $L\oplus L$ is determined by $L$. The Möbius transformation of the regular matrix is that of its $2\times2$ block, and the doubling adds no parameter.

### The Idempotents

**The regular display.** The rank-two idempotents of the image are the doubles $\tfrac12(\Pi\oplus\Pi)$ of the rank-one idempotents, or more generally $\Pi\oplus\Pi$ with $\Pi$ a rank-one idempotent. They form a two-dimensional family inside the eight-dimensional ambient conjugacy class of rank-two projectors. The fibre over a line is again an affine line.

### The Action

**The regular display.** The same formula holds for the doubled ideals: $M J_L=J_{ML}$. The kernel is $\mathbb{C}^{\times}\mathrm I_4$, and the quotient is again $PGL_2(\mathbb{C})$; the action on the line is the same, and only the rank of the ideals changes.

## Summary

The minimal ideals are the sets $I_L$ of matrices whose image lies in $L$, and $L\mapsto I_L$ is a bijection between $\mathbb{P}^1(\mathbb{C})$ and the middle layer of the lattice; in the regular model the ideals are the doubled sets $J_L$, of rank two, parametrised by the same line. The group of units acts by $M\cdot I_L=I_{ML}$, with kernel the scalar matrices, so the action is that of $PGL_2(\mathbb{C})$. In the chart $z=\xi_1/\xi_2$ the action is $z\mapsto(az+b)/(cz+d)$, with $I_{L_0}$ at $0$ and $I_{L_\infty}$ at $\infty$. The rank-one idempotents fibre over the line with an affine line of kernels, the action is simply transitive on ordered triples, and the cross-ratio is the complete invariant of a quadruple. Coefficient conjugation acts by $z\mapsto-1/\bar z$, with no fixed point.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I_L=\{M:\operatorname{im}M\subseteq L\}$ | the minimal left ideal of the line $L$ |
| $J_L$ | the doubled minimal ideal, of rank two |
| $\mathbb{P}^1(\mathbb{C})$ | the projective line of lines of $\mathbb{C}^2$ |
| $M\cdot L=ML$ | the action of $GL_2(\mathbb{C})$ |
| $\mathbb{C}^{\times}\mathrm I$ | the kernel of the action |
| $PGL_2(\mathbb{C})$ | the Möbius group, the automorphism group |
| $z=\xi_1/\xi_2$ | the affine chart |
| $[z_1,z_2;z_3,z_4]$ | the cross-ratio |
| $[\xi,\eta]=\det(\xi,\eta)$ | the Plücker bracket |
| $\epsilon$ | the matrix of the quaternionic structure |
| $z\mapsto-1/\bar z$ | the induced coefficient conjugation |

## Further Reading

- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the two coordinate ideals
- [Matrix Representations : The Conjugations and the Adjoints](matrix-representations-the-conjugations-and-the-adjoints.html), for the real structure
- [Matrix Representations : The Centraliser and the Double Centraliser](matrix-representations-the-centraliser-and-the-double-centraliser.html), for the module structure
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the displays
- [The Category of Modules](the-category-of-modules.html), for the module reading