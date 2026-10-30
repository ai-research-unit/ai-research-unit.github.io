# __$M_4(\mathbb{C})$ Representation : The Projective Line and the Möbius Action__

## Introduction

The minimal left ideals of the biquaternion algebra form a projective line, and the unit group acts on that line by right multiplication. Their adjoint mirrors, the minimal right ideals, are the sets of matrices whose image lies in a fixed line; on them the group acts by left multiplication, and in a chart the action is the Möbius action of $PGL_2(\mathbb{C})$. In the regular model the right ideals are rank-two ideals of $M_4(\mathbb{C})$ of the form $W\oplus W$. The parameter space is the same $\mathbb{P}^1$ as in the $2\times2$ model; what doubles is the rank of the ideals and the size of the matrices.

This article develops the parametrisation, the action and its kernel, the chart and the Möbius formula, the idempotents, the orbits and the cross-ratio. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Projective Line and the Möbius Action*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. A vector of $\mathbb{C}^2$ is a column $\xi$, a line is written $[\xi]$, and the projective line is $\mathbb{P}^1(\mathbb{C})$. The chart is $z=\xi_1/\xi_2$ on the open set $\xi_2\neq0$. The regular matrices are written in the eigenbasis, where $\mathsf{M}_4^{L}(\tilde Q)=\operatorname{diag}(A,A)$ with $A=\mathsf{M}_2(\tilde Q)$.

**Boundaries.** The lattice of ideals and the parametrisation by $\mathbb{P}^1$ are *The Category of Modules*, §*The Lattice of Left Ideals*; the automorphism group is *Biquaternion Automorphisms and Derivations*; the real structure is *The Category of Modules*, §*The Projective Line and the Möbius Action*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Projective Line and the Möbius Action*.

**Frame.** Unless a basis is named, matrices are written in the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, where $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display: $\mathsf M_{4,\mathrm{coef}}^{L}=S\,(I_2\otimes\mathsf M_2)\,S^{-1}$, with $S$ the change of *The Product, the Trace and the Determinant*.

## The Lines and the Minimal Left Ideals

For a line $L\in\mathbb{P}^1(\mathbb{C})$ put
$$
J_L=\{M\in\mathsf{M}_4^{L}(\mathbb{B}):\operatorname{im}M\subseteq L\oplus L\}.
$$
The adjoint $J_L^{\dagger}=\{M^{\dagger}:M\in J_L\}$ is a minimal left ideal. The two families are exchanged by the dagger, and they define the same projective line; the computation below is stated for the right ideals because left multiplication then gives the standard Möbius formula, and the left-ideal statement is the adjoint read backwards.

**Proposition.** $J_L$ is a minimal right ideal of the regular image, and every minimal right ideal of the image is $J_L$ for a unique $L$.

*Proof.* The set $J_L$ is a right ideal, because $\operatorname{im}(MN)\subseteq\operatorname{im}M\subseteq L\oplus L$ for every $N$ in the image. In the eigenbasis it is the set of block matrices $\operatorname{diag}(A,A)$ with $\operatorname{im}A\subseteq L$, a complex subspace of dimension two. A nonzero element has rank two, and the right ideal it generates is the whole of $J_L$, so $J_L$ is minimal. Conversely, a minimal right ideal of the image is the image of a minimal right ideal of the algebra, which is $J_L$ for a unique line.

**The two coordinate ideals.** With $L_\infty=\operatorname{span}\{e_1\}$ and $L_0=\operatorname{span}\{e_2\}$,
$$
J_{L_\infty}=\left\{\operatorname{diag}\begin{pmatrix}a&b\\0&0\end{pmatrix}:a,b\in\mathbb{C}\right\},
\qquad
J_{L_0}=\left\{\operatorname{diag}\begin{pmatrix}0&0\\c&d\end{pmatrix}:c,d\in\mathbb{C}\right\}.
$$
These are the adjoint mirrors of the two minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ of the Peirce decomposition. Each is a two-dimensional complex subspace of $M_4(\mathbb{C})$, and its nonzero elements have rank two.

**The rank.** In the $2\times2$ model a minimal right ideal consists of rank-one matrices; in the regular model it consists of rank-two matrices. The rank doubles with the size, and the parameter line does not.

## The Action of $GL_2(\mathbb{C})$

For $M\in\mathsf{M}_4^{L}(\mathbb{B}^{\times})$ and a line $L$, put
$$
M\cdot L=ML.
$$

**Proposition.** The product is a line, and the assignment is an action of the unit group on $\mathbb{P}^1(\mathbb{C})$:
$$
M\cdot J_L=J_{ML},\qquad M_1\cdot(M_2\cdot L)=(M_1M_2)\cdot L.
$$

*Proof.* An invertible matrix carries a one-dimensional subspace to a one-dimensional subspace, and the second statement is associativity of the matrix product. In the eigenbasis $M=\operatorname{diag}(A,A)$ acts on $L\oplus L$ as $A$ acts on $L$.

**The kernel.** If $M$ acts trivially on every line, then every vector is an eigenvector of $M$, and a matrix with that property is scalar. Hence
$$
\ker=\mathbb{C}^{\times}\mathrm I_4,
\qquad
\mathsf{M}_4^{L}(\mathbb{B}^{\times})/\mathbb{C}^{\times}\mathrm I_4\cong PGL_2(\mathbb{C}).
$$
The action factors through $PGL_2(\mathbb{C})$, which is the automorphism group of $M_2(\mathbb{C})$ and, by transport, of the biquaternion algebra. On idempotents the same action reads
$$
\Pi\longmapsto M\Pi M^{-1},
$$
because $M J_{\operatorname{im}\Pi}=J_{M\operatorname{im}\Pi}=J_{\operatorname{im}(M\Pi M^{-1})}$.

**The two copies.** The regular matrix acts on the two copies of $\mathbb{C}^2$ by the same matrix $A$, so the Möbius transformation on the projective line is the same on both copies. The regular model doubles the spinor space but not the projective parameter space.

**The left mirror.** The left ideals are the adjoints $J_L^{\dagger}$. Since $(MN)^{\dagger}=N^{\dagger}M^{\dagger}$, the group acts on them by right multiplication, and the matrix of the action is the transpose. The Möbius formula below is written for the right ideals; on the left ideals it is the contragredient formula with $A^{\mathsf T}$. The two actions have the same orbits and the same cross-ratio.

## The Chart and the Möbius Formula

Write a line by the column $\xi=(z,1)^{\mathsf T}$, with $z=\xi_1/\xi_2$, and let
$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad ad-bc\neq0.
$$
Then
$$
A\xi=\begin{pmatrix}az+b\\ cz+d\end{pmatrix},
\qquad
z'=\frac{az+b}{cz+d},
$$
which is the **Möbius transformation** attached to $A$. A nonzero scalar multiple of $A$ gives the same transformation, so the formula depends only on the class $[A]\in PGL_2(\mathbb{C})$, and composition of transformations is multiplication of matrices:
$$
\varphi_{A_1}\circ\varphi_{A_2}=\varphi_{A_1A_2}.
$$
In the regular model the matrix is $\operatorname{diag}(A,A)$, and the transformation on each copy is $\varphi_A$.

**The two coordinate points.** In this chart $J_{L_0}$ sits at $z=0$ and $J_{L_\infty}$ at $z=\infty$: the point at infinity is the line of the first basis vector. The two ideals are exchanged by the Möbius map $z\mapsto-1/z$, the image of the matrix $\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.

## The Idempotents

A **rank-two idempotent of the image** is a matrix $\Pi\neq0$ with $\Pi^2=\Pi$ and $\operatorname{rk}\Pi=2$ that lies in the image. Its image is a subspace $W\oplus W$ and its kernel is a subspace $K\oplus K$ with $W\neq K$, and it is the projection onto $W\oplus W$ along $K\oplus K$.

**Proposition.** Every rank-two idempotent of the image with image $W\oplus W$ and kernel $K\oplus K$ is
$$
\Pi=\mathsf{M}_4^{L}(u\eta),
$$
where $u$ spans $W$ and $\eta$ is the linear form with $\eta(u)=1$ and $\eta(K)=0$. The fibre of the map $\Pi\mapsto\operatorname{im}\Pi$ over $W$ is an affine line, parametrised by the kernel $K\neq W$.

*Proof.* The product $u\eta$ satisfies $(u\eta)^2=u\eta(u)\eta=u\eta$, has image $W$ and kernel $K$. Its image under $\mathsf{M}_4^{L}$ is a rank-two idempotent with image $W\oplus W$ and kernel $K\oplus K$. Conversely a rank-two idempotent of the image with image $W\oplus W$ is determined by its kernel, and the formula recovers it. The kernels $K\neq W$ form the affine line $\mathbb{P}^1\setminus\{W\}$.

**The conjugacy class.** Every rank-two idempotent of the image is conjugate, in the image, to $\operatorname{diag}(1,1,0,0)$. The image of the $GL_2$ action is transitive on the pairs (image, kernel) of lines, and the stabiliser of the standard idempotent is the diagonal torus of complex dimension two. The class in the image therefore has complex dimension two. In the ambient $GL_4$ the same projector has an eight-dimensional conjugacy class, because the image and the kernel can vary independently in $\mathbb{C}^4$; the image is the two-dimensional subfamily with image and kernel of the form $W\oplus W$ and $K\oplus K$.

**The four corners.** The two idempotents $\operatorname{diag}(1,1,0,0)$ and $\operatorname{diag}(0,0,1,1)$ are orthogonal and sum to $\mathrm I_4$; they are the two coordinate points of the chart. The Peirce decomposition of the regular algebra is the decomposition into the four $2\times2$ blocks.

## Orbits, Stabilisers and the Cross-Ratio

**Transitivity.** The action is transitive: any two lines are carried to one another by an invertible matrix. The stabiliser of $z=0$ is the set of matrices with $b=0$,
$$
\left\{\begin{pmatrix}a&0\\c&d\end{pmatrix}:ad\neq0\right\},
$$
a Borel subgroup of $PGL_2(\mathbb{C})$, of complex dimension two.

**Triple transitivity.** The action is simply transitive on ordered triples of distinct points. A matrix is determined up to scalar by the images of three lines, and any three distinct lines can be sent to any other three.

**The cross-ratio.** For four distinct points the quantity
$$
[z_1,z_2;z_3,z_4]=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}
$$
is invariant under every Möbius transformation, and it is the complete invariant of a quadruple: two quadruples are equivalent under $PGL_2(\mathbb{C})$ exactly when their cross-ratios agree.

**The meaning for the ideals.** The cross-ratio of four minimal right ideals is the invariant of their configuration, and the three-transitivity says that any ordered triple of distinct minimal ideals can be normalised to the triple $(0,1,\infty)$ by a unique automorphism of the algebra. The regular model doubles the ideals but not their configurations: the cross-ratio is computed on the same line.

## The Plücker Form of the Cross-Ratio

**The bracket.** For two vectors $\xi,\eta\in\mathbb{C}^2$, put
$$
[\xi,\eta]=\det(\xi,\eta)=\xi_1\eta_2-\xi_2\eta_1.
$$
The bracket is alternating and $\mathbb{C}$-bilinear, and $[\xi,\eta]\neq0$ exactly when the two lines are distinct.

**The cross-ratio.** For four vectors with nonzero brackets,
$$
[\xi_1,\xi_2;\xi_3,\xi_4]
=\frac{[\xi_1,\xi_3]\,[\xi_2,\xi_4]}
{[\xi_1,\xi_4]\,[\xi_2,\xi_3]}.
$$
In the chart $\xi_i=(z_i,1)^{\mathsf T}$ this is the cross-ratio formula of the preceding section, because $[\xi_i,\xi_j]=z_i-z_j$.

**Invariance in the regular model.** For $M=\mathsf{M}_4^{L}(\tilde Q)$ acting on $L\oplus L$ by the same $2\times2$ matrix $A$ on each copy,
$$
[M\xi,M\eta]=\det(A)\,[\xi,\eta]=N\,[\xi,\eta],
$$
so every bracket in the numerator and the denominator is multiplied by the same determinant, and the cross-ratio is unchanged. The determinant of the $4\times4$ matrix is $N^2$, and the two copies contribute the same factor; the bracket itself is computed in one copy, with determinant $N$.

**Normalisation.** Three distinct lines can be sent to the three coordinate points, and the remaining freedom is the one complex parameter of the fourth line. In a basis $(\xi_1,\xi_2)$ with $\xi_3=\xi_1+\xi_2$ and $\xi_4=c\xi_1+d\xi_2$, the parameter is $c/d$, and it is the cross-ratio $[\xi_1,\xi_2;\xi_3,\xi_4]$.

## The Real Structure

**The real form.** On the real quaternion subspace the unit-norm group is $SU(2)$, and the projective line of complex lines is replaced by the sphere of real directions. The quotient of $SU(2)$ by its centre is $SO(3)$, and the action on the real projective line is the rotation action on the Bloch sphere. The regular model carries two copies of the spinor space, and the two copies give the same Bloch vector in *$M_4(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

**The compact picture.** The compact real form of $PGL_2(\mathbb{C})$ is $PU(2)\cong SO(3)$, and the projective line with its real structure is the two-sphere. The Möbius action restricts to the rotation action, and the cross-ratio restricts to the conformal invariant of four points on the sphere.

## Summary

The minimal right ideals of the regular image are the rank-two ideals $J_L=\{M:\operatorname{im}M\subseteq L\oplus L\}$, parametrised by the same projective line $\mathbb{P}^1(\mathbb{C})$ as in the $2\times2$ model. The unit group acts by left multiplication, with kernel $\mathbb{C}^{\times}\mathrm I_4$ and quotient $PGL_2(\mathbb{C})$. In a chart the action is the Möbius transformation $z\mapsto(az+b)/(cz+d)$. The rank-two idempotents of the image form a two-dimensional family, embedded in the eight-dimensional ambient conjugacy class. The action is triply transitive, and the cross-ratio is the complete invariant of four ideals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_L=\{M:\operatorname{im}M\subseteq L\oplus L\}$ | the minimal right ideal of the image |
| $L\in\mathbb{P}^1(\mathbb{C})$ | the line, the parameter |
| $PGL_2(\mathbb{C})$ | the quotient of the unit group by the scalars |
| $z\mapsto(az+b)/(cz+d)$ | the Möbius action |
| $\operatorname{diag}(1,1,0,0)$ | the standard rank-two idempotent |
| $[z_1,z_2;z_3,z_4]$ | the cross-ratio |

## Further Reading

- [$M_4(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the two columns
- [$M_4(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](m4c-representation-spin-qubits-and-the-bloch-vector.html), for the real picture
- [$M_2(\mathbb{C})$ Representation : The Projective Line and the Möbius Action](m2c-representation-the-projective-line-and-the-mobius-action.html), for the $2\times2$ version
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the lattice of ideals
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the automorphism group
