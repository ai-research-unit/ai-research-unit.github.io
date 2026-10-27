# __$M_2(\mathbb{R})$ Model : The Subspaces as Matrix Conditions__

## Introduction

The defining representation of *Split-Quaternion Matrix Element Representations* is an isomorphism $\mathsf{M}_2 : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$, not an injection into a larger ring. Every linear subspace of the algebra is therefore a linear subspace of $M_2(\mathbb{R})$, and every statement about a subspace can be read as a matrix condition.

This article tabulates those conditions for the distinguished subspaces of the category. It identifies the scalar line and the vector subspace, the three two-dimensional subalgebras through the identity, the symmetric and the skew-symmetric parts, and the coordinate dictionary that converts between the split-quaternion coordinates $(q_t,q_x,q_y,q_z)$ and the matrix entries $(a,b,c,d)$. The computations are those of the model; no form, no norm and no topology are used.

The subspaces themselves are the subject of *Split-Quaternion Scalar and Vector Subspaces*, *Split-Quaternion Split-Complex Subspaces* and *Split-Quaternion Subspaces and the Involutions*. The Peirce decomposition is *Split-Quaternion Ideals and Peirce Decomposition*, and its matrix form is the companion article *$M_2(\mathbb{R})$ Model : The Idempotents and the Peirce Decomposition*.

## The Coordinate Dictionary

**Definition.** The model is

$$
\mathsf{M}_2(q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z) = \begin{pmatrix} q_t - q_z & q_y - q_x \\ q_x + q_y & q_t + q_z \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.
$$

The four matrix entries and the four split-quaternion coordinates carry the same information, and the conversion is linear.

**Proposition (the dictionary).** For every element $\tilde q$,

$$
a = q_t - q_z, \qquad b = q_y - q_x, \qquad c = q_x + q_y, \qquad d = q_t + q_z,
$$

and conversely

$$
q_t = \tfrac12(a+d), \qquad q_x = \tfrac12(c-b), \qquad q_y = \tfrac12(b+c), \qquad q_z = \tfrac12(d-a).
$$

**Proof.** The first four identities are the definition read entry by entry. Adding and subtracting the pairs gives the second four: $a+d=2q_t$, $d-a=2q_z$, $c-b=2q_x$ and $b+c=2q_y$.

The dictionary is invertible because the two quadruples have the same dimension and the change of basis is the invertible matrix

$$
\begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & -1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} q_t \\ q_x \\ q_y \\ q_z \end{pmatrix}.
$$

**Example.** The element $\tilde q = 3 + 2\vec e_x - \vec e_y + 5\vec e_z$ has matrix

$$
\mathsf{M}_2(\tilde q) = \begin{pmatrix} 3-5 & -1-2 \\ 2-1 & 3+5 \end{pmatrix} = \begin{pmatrix} -2 & -3 \\ 1 & 8 \end{pmatrix},
$$

and the dictionary returns $q_t = \tfrac12(6)=3$, $q_x=\tfrac12(1+3)=2$, $q_y=\tfrac12(-3+1)=-1$ and $q_z=\tfrac12(8+2)=5$.

## The Scalar Line and the Vector Subspace

**Proposition (the scalar line).** The fixed space of the conjugation is the line of scalar matrices:

$$
S = \{\tilde q : \tilde{q}^{\natural}=\tilde q\} = \mathbb{R}e_t \;\longleftrightarrow\; \{q_t I : q_t \in \mathbb{R}\}.
$$

**Proof.** The scalar part of $\tilde q$ is $q_t e_t$, and $\mathsf{M}_2(q_t e_t)=q_t I$ by the dictionary, with $a=d=q_t$ and $b=c=0$. Conversely $q_x=q_y=q_z=0$ is read from $b=c=0$ and $a=d$.

**Proposition (the vector subspace).** The anti-fixed space of the conjugation is the space of traceless matrices:

$$
V = \{\tilde q : \tilde{q}^{\natural}=-\tilde q\} = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\} \;\longleftrightarrow\; \{M : \operatorname{tr}M = 0\}.
$$

**Proof.** By the dictionary, $\operatorname{tr}\mathsf{M}_2(\tilde q)=a+d=2q_t$. The trace vanishes exactly when $q_t=0$, which is the defining condition of $V$.

The two propositions give the matrix form of the scalar–vector decomposition

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V \;\longleftrightarrow\; M_2(\mathbb{R}) = \mathbb{R}I \oplus \mathfrak{sl}_2(\mathbb{R}),
$$

the second summand being the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$ of traceless matrices. The decomposition is orthogonal for the trace form of the companion article *$M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints*, since $\operatorname{tr}I=2$ and $\operatorname{tr}M=0$ for $M\in\mathfrak{sl}_2(\mathbb{R})$.

## The Three Planes Through the Identity

**Theorem (the three coordinate planes).** The three coordinate planes through the identity are subalgebras, and in the model they are:

| subalgebra | matrix condition | type |
|---|---|---|
| $\operatorname{span}\{1,\vec e_x\}$ | $M = aI + bJ$, equivalently $[M,J]=0$ | $\mathbb{C}$ |
| $\operatorname{span}\{1,\vec e_y\}$ | $M = aI + bK$, equivalently $M=M^{\mathsf T}$ with equal diagonal entries | $\mathbb{R}\times\mathbb{R}$ |
| $\operatorname{span}\{1,\vec e_z\}$ | $M = \operatorname{diag}(a,b)$ | $\mathbb{R}\times\mathbb{R}$ |

**Proof.** Each plane is closed under multiplication because the square of its vector generator is central: $\vec e_x^2=-1$, $\vec e_y^2=1$ and $\vec e_z^2=1$. The three types follow from those signs: a real algebra generated by $1$ and $j$ with $j^2=-1$ is $\mathbb{C}$, and with $j^2=+1$ it is $\mathbb{R}\times\mathbb{R}$ through the idempotents $\tfrac12(1\pm j)$.

The matrix conditions are read from the dictionary. For $M=aI+bJ$ the entries are $a=d$, $c=-b$; commutation with $J$ is the pair of identities $a=d$ and $c=-b$, which is the same condition. For $M=aI+bK$ the entries are $a=d$ and $b=c$, which is symmetry together with the equality of the diagonal entries. For $M$ diagonal the entries $b$ and $c$ vanish, that is $q_x=q_y=0$.

**Remark (the planes are not the only ones).** Every plane $\operatorname{span}\{1,\tilde v\}$ with $\tilde v$ pure is a subalgebra, because $\tilde v^2=-N(\tilde v)e_t$ is scalar for a pure element. The type depends only on the sign of the norm of $\tilde v$:

| $N(\tilde v)$ | $\tilde v^2$ | type |
|---|---|---|
| $+1$ | $-1$ | $\mathbb{C}$ |
| $0$ | $0$ | the dual numbers $\mathbb{R}[\varepsilon]/(\varepsilon^2)$ |
| $-1$ | $+1$ | $\mathbb{R}\times\mathbb{R}$ |

So the algebra carries a two-parameter family of planes through the identity, of three isomorphism types, and the three coordinate planes above are one representative of each type together with a second representative of the split type. The complex plane of the model is the case $N(\tilde v)=+1$; the two split planes are the cases $N(\tilde v)=-1$.

The three planes are the complex and the two split-complex readings of the algebra. The first is the conformal plane of *Complex Regular Element Representation*: $aI+bJ$ is the matrix of multiplication by $a+bi$, the composition of a scaling and a rotation. In the second, $aI+bK$ with $a^2-b^2\neq0$ is a hyperbolic rotation, and the two idempotents are the rank-one projections of the next article. In the third, $\operatorname{diag}(a,b)$ is a pair of independent scalings, one on each axis.

**Remark (the planes and the involutions).** The principal involution $\alpha$ fixes the plane $\operatorname{span}\{1,\vec e_z\}$ pointwise and acts as $-1$ on $\operatorname{span}\{\vec e_x,\vec e_y\}$. The reversal $\rho$ fixes the three-dimensional space $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ and negates $\mathbb{R}\vec e_z$. The conjugation fixes only the scalar line. None of the three fixes the plane $\operatorname{span}\{1,\vec e_x\}$ pointwise, so the complex plane of the model is not one of the eigenspaces of *Split-Quaternion Subspaces and the Involutions*.

## The Symmetric and the Skew-Symmetric Parts

**Proposition (the symmetric part).** A matrix $\mathsf{M}_2(\tilde q)$ is symmetric exactly when $q_x=0$:

$$
\mathsf{M}_2(\tilde q)^{\mathsf T} = \mathsf{M}_2(\tilde q) \;\Longleftrightarrow\; \tilde q \in \operatorname{span}\{1,\vec e_y,\vec e_z\}.
$$

**Proof.** Symmetry is $b=c$, that is $q_y-q_x=q_x+q_y$, which is $2q_x=0$. The remaining coordinates $q_t,q_y,q_z$ are free, giving the three-dimensional space.

**Proposition (the skew-symmetric part).** A matrix $\mathsf{M}_2(\tilde q)$ is skew-symmetric exactly when $\tilde q$ lies on the line $\mathbb{R}\vec e_x$:

$$
\mathsf{M}_2(\tilde q)^{\mathsf T} = -\mathsf{M}_2(\tilde q) \;\Longleftrightarrow\; \tilde q = q_x\vec e_x.
$$

**Proof.** Skew-symmetry is $a=d=0$ and $b=-c$. The first pair gives $q_t=q_z=0$; the second gives $q_y-q_x=-q_x-q_y$, that is $2q_y=0$. Only $q_x$ remains.

The two propositions give the decomposition of an element into its symmetric and antisymmetric parts:

$$
\mathsf{M}_2(\tilde q) = \mathsf{M}_2(q_t e_t + q_y\vec e_y + q_z\vec e_z) - q_x\vec e_x,
$$

since the antisymmetric part of $\mathsf{M}_2(\tilde q)$ is

$$
\tfrac12\bigl(\mathsf{M}_2(\tilde q)-\mathsf{M}_2(\tilde q)^{\mathsf T}\bigr) = \tfrac12\begin{pmatrix} 0 & b-c \\ c-b & 0 \end{pmatrix} = \tfrac12(c-b)J = -q_x\vec e_x.
$$

The symmetric summand is the part supported on $\operatorname{span}\{1,\vec e_y,\vec e_z\}$, and the skew summand is the part supported on the complex line $\mathbb{R}\vec e_x$.

**Remark (no subalgebra).** Neither part is a subalgebra. The product of two symmetric matrices need not be symmetric, since $KD=-J$ is not symmetric, and the skew line is not closed because $\vec e_x^2=-1$ is scalar. The smallest subalgebra containing the skew line is the complex plane $\operatorname{span}\{1,\vec e_x\}$.

## Summary

The defining representation converts every distinguished subspace of the split-quaternion algebra into a matrix condition. The scalar line is the line of scalar matrices, the vector subspace is the space of traceless matrices, and the three two-dimensional subalgebras through the identity are the conformal plane $aI+bJ\cong\mathbb{C}$, the symmetric plane $aI+bK\cong\mathbb{R}\times\mathbb{R}$ and the diagonal plane $\cong\mathbb{R}\times\mathbb{R}$.

The symmetric matrices are exactly the elements with vanishing $q_x$, a three-dimensional space $\operatorname{span}\{1,\vec e_y,\vec e_z\}$, and the skew-symmetric matrices are exactly the line $\mathbb{R}\vec e_x$. The antisymmetric part of $\mathsf{M}_2(\tilde q)$ is $-q_x\vec e_x$, so the decomposition into symmetric and skew parts is the decomposition of the element along the complex line and its complement.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the defining isomorphism $\mathbb{H}_{\mathrm{s}}\to M_2(\mathbb{R})$ | *Split-Quaternion Matrix Element Representations* |
| $a,b,c,d$ | the entries of $\mathsf{M}_2(\tilde q)$ | this article |
| $J,K,D$ | the images of $\vec e_x,\vec e_y,\vec e_z$ | *Split-Quaternion Matrix Element Representations* |
| $S$ | the scalar line, the scalar matrices | *Split-Quaternion Scalar and Vector Subspaces* |
| $V$ | the vector subspace, the traceless matrices | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathfrak{sl}_2(\mathbb{R})$ | the traceless matrices, the image of $V$ | *Split-Quaternion Algebra* |
| $\alpha,\rho,{}^{\natural}$ | the principal involution, the reversal, the conjugation | *Split-Quaternion Subspaces and the Involutions* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix units and the subspace lattice of a matrix algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ and its subalgebras.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for explicit matrix models of the low-dimensional Clifford algebras.
