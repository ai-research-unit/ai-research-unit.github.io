# __$M_2(\mathbb{R})$ Standard Representation__

## Introduction

**The model is the algebra.** The split-quaternion algebra $\mathbb{H}_{\mathrm{spl}}$ is four-dimensional over $\mathbb{R}$ and so is $M_2(\mathbb{R})$, and the defining map of this article is an isomorphism between them. Nothing is lost and nothing is added: every split quaternion is a $2\times2$ real matrix, every such matrix is a split quaternion, and the two products are the same product. This is the sharpest contrast in the whole family of models. The quaternions embed in $M_2(\mathbb{C})$ as a four-real-dimensional subspace of an eight-dimensional algebra; the split-biquaternions embed in the diagonal of $M_2(\mathbb{H})$ and leave the off-diagonal entries empty; here the image fills the target.

**Why the split case is where the model is transparent.** A matrix model of an algebra carries two structures at once, the algebra structure and the action on a plane. When the model is surjective the two coincide in the simplest possible way, because the plane is the algebra and the action is the product. Every invariant of the element becomes an invariant of its matrix with no remainder: the norm becomes the determinant, twice the scalar part becomes the trace, the conjugations become the adjugate and the transpose, the idempotents become the rank-one projections, and the zero divisors become the singular matrices. The article follows that correspondence section by section, and each section names what the correspondence does **not** preserve, since the exceptions are where the algebra differs from a generic matrix algebra.

**What the model costs.** Two properties of the algebra become less visible rather than more. The first is the trace: the matrix trace of an element is twice its scalar part, so the scalar part is half the trace and no matrix statement names the scalar part directly. The second is the signature: the determinant is a form of signature $(2,2)$, and a matrix algebra over $\mathbb{R}$ has no intrinsic reason to prefer it, so the model hides that the algebra is $\mathrm{Cl}_{1,1}$ and not $\mathrm{Cl}_{2,0}$. Both costs are paid once and are then harmless.

**Boundaries.** The algebra, its multiplication table, its centre, its simplicity and its units are *Split-Quaternion Algebra* and *Split-Quaternion Norm and Invertibility*; the element, its coordinates and its involutions are *Split-Quaternion Subspaces and the Involutions*. The zero divisors are *Split-Quaternion Zero Divisors*, the spectrum and its degeneracies are *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*, the modules are *Split-Quaternion Linear Representations*, and the projective geometry of the null quadric is *Split-Quaternion Null Quadric and Projective Geometry*. The operators of the model, one-sided and two-sided, are the companion article *$M_2(\mathbb{R})$ Standard Representation : Operators*.

**Conventions.** The basis of the algebra is $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with

$$
\vec e_x^2=-e_t,\qquad \vec e_y^2=\vec e_z^2=e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\qquad \vec e_y\vec e_z=-\vec e_x,\qquad \vec e_z\vec e_x=\vec e_y,
$$

and the reversed products opposite, so $\vec e_y\vec e_x=-\vec e_z$, $\vec e_z\vec e_y=\vec e_x$, $\vec e_x\vec e_z=-\vec e_y$. An element is $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, its scalar part is $q_t$, its pure part is $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, and its split-quaternion norm is

$$
\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2-q_y^2-q_z^2 .
$$

The matrix units of $M_2(\mathbb{R})$ are $E_{ij}$, the identity is $I$, and $\operatorname{tr}$, $\det$, $\operatorname{adj}$ are the matrix trace, determinant and adjugate.

## The Model

**Definition.** The **defining representation** is the linear map $\mathsf{M}_2:\mathbb{H}_{\mathrm{spl}}\to M_2(\mathbb{R})$ fixed on the basis by

$$
\mathsf{M}_2(e_t)=I,\qquad
\mathsf{M}_2(\vec e_x)=J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=K=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=D=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$

**The dictionary.** On a general element the map is

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_t-q_z & q_y-q_x\\ q_x+q_y & q_t+q_z\end{pmatrix},
$$

and it inverts by

$$
q_t=\tfrac12\operatorname{tr}\mathsf{M}_2(\tilde q),\qquad
q_z=\tfrac12\bigl(M_{22}-M_{11}\bigr),\qquad
q_x=\tfrac12\bigl(M_{21}-M_{12}\bigr),\qquad
q_y=\tfrac12\bigl(M_{21}+M_{12}\bigr).
$$

The two off-diagonal entries mix $q_x$ and $q_y$ with opposite signs, and that crossing is the only thing the model does that a naive coordinate reading would miss.

**The check.** The four images multiply as the four generators do, and the verification is one line each. Squaring, $J^2=-I$ reproduces $\vec e_x^2=-e_t$, while $K^2=D^2=I$ reproduce $\vec e_y^2=\vec e_z^2=e_t$. Multiplying, $JK=D$ reproduces $\vec e_x\vec e_y=\vec e_z$, and $KD=-J$, $DJ=K$ reproduce the other two products.

**Theorem (the model is an isomorphism).** The map $\mathsf{M}_2$ is an isomorphism of real algebras,

$$
\mathbb{H}_{\mathrm{spl}}\;\cong\;M_2(\mathbb{R}),
$$

and in particular it is surjective.

**Proof.** Linearity is by definition, multiplicativity follows from the multiplication table as checked above, injectivity from the linear independence of the four images, and surjectivity from the equality of the dimensions, $4=4$.

**Corollary (the least degree).** The least degree of a faithful real matrix representation of $\mathbb{H}_{\mathrm{spl}}$ is two.

**Proof.** A faithful representation of degree $n$ embeds a four-dimensional algebra into $M_n(\mathbb{R})$ of dimension $n^2$, so $n^2\ge4$; $n=1$ is excluded because $M_1(\mathbb{R})$ is commutative and $\mathbb{H}_{\mathrm{spl}}$ is not; degree two is attained by $\mathsf{M}_2$.

**Uniqueness up to conjugacy.** Every unital algebra homomorphism $\Psi:\mathbb{H}_{\mathrm{spl}}\to M_2(\mathbb{R})$ is an isomorphism, and there is $P\in GL_2(\mathbb{R})$ with $\Psi(\tilde q)=P\mathsf{M}_2(\tilde q)P^{-1}$ for every $\tilde q$. The kernel of $\Psi$ is a two-sided ideal, the algebra is simple, so the kernel is zero; then $\Psi\mathsf{M}_2^{-1}$ is an automorphism of $M_2(\mathbb{R})$, and by Skolem–Noether every such automorphism is inner. The consequence is the rule of the whole category: **one model, and it is unique**, so every statement below is a statement about the algebra and not about a choice.

**The automorphisms.** The same argument gives

$$
\operatorname{Aut}(\mathbb{H}_{\mathrm{spl}})\cong\mathrm{PGL}_2(\mathbb{R}),
\qquad \alpha_g(\tilde q)=g\tilde qg^{-1},\quad g\in{\mathbb{H}_{\mathrm{spl}}}^{\times},
$$

with $g$ and $\lambda g$ inducing the same automorphism because the centre is $\mathbb{R}e_t$.

**The dictionary of the four elements.** The table collects the four basis elements, their images, their squares and their ranks.

| element | matrix | square | trace | determinant | rank |
|---|---|---|---|---|---|
| $e_t$ | $I$ | $I$ | $2$ | $1$ | $2$ |
| $\vec e_x$ | $J$ | $-I$ | $0$ | $1$ | $2$ |
| $\vec e_y$ | $K$ | $I$ | $0$ | $-1$ | $2$ |
| $\vec e_z$ | $D$ | $I$ | $0$ | $-1$ | $2$ |

The four are units, and the table already shows the two opposite behaviours the algebra mixes: $\vec e_x$ is a complex structure, of determinant $+1$, while $\vec e_y$ and $\vec e_z$ are reflections, of determinant $-1$.

## The Left and the Right Matrices

**Definition.** The algebra acts on itself by left and right multiplication, $L_{\tilde q}(\tilde x)=\tilde q\tilde x$ and $R_{\tilde q}(\tilde x)=\tilde x\tilde q$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ these are $4\times4$ real matrices, and in the model they read

$$
L_{\tilde q}=M_{\tilde q}\otimes I_2,\qquad R_{\tilde q}=I_2\otimes M_{\tilde q}^{\mathsf T},
$$

where the tensor product is taken in the row-major vectorisation of $M_2(\mathbb{R})$, so that $\operatorname{vec}(AXB)=(A\otimes B^{\mathsf T})\operatorname{vec}X$.

**The two copies.** The maps $\tilde q\mapsto L_{\tilde q}$ and $\tilde q\mapsto R_{\tilde q}$ are two isomorphisms of $\mathbb{H}_{\mathrm{spl}}$ onto two four-dimensional subalgebras of $M_4(\mathbb{R})$. They are different subalgebras, because the algebra is not commutative: $L_{\tilde q}=R_{\tilde q}$ holds exactly for the central elements, that is for the scalar multiples of $e_t$.

**The product rule.** For all $\tilde q,\tilde p,\tilde x$,

$$
L_{\tilde q}L_{\tilde p}=L_{\tilde q\tilde p},\qquad
R_{\tilde q}R_{\tilde p}=R_{\tilde p\tilde q},\qquad
L_{\tilde q}R_{\tilde p}=R_{\tilde p}L_{\tilde q}.
$$

The third identity is associativity, and it is the one that matters for the operators article: the two families commute, each is the centraliser of the other inside $M_4(\mathbb{R})$, and $M_4(\mathbb{R})=M_2(\mathbb{R})\otimes M_2(\mathbb{R})$ is the enveloping algebra of the pair.

**The rank.** By the rank rule for a Kronecker product,

$$
\operatorname{rank}L_{\tilde q}=2\operatorname{rank}M_{\tilde q},\qquad
\operatorname{rank}R_{\tilde q}=2\operatorname{rank}M_{\tilde q},
$$

so the left and right matrices share the rank, and that rank is $4$ on the units, $2$ on the nonzero zero divisors and $0$ at the origin. The trace is $\operatorname{tr}L_{\tilde q}=2\operatorname{tr}M_{\tilde q}=4q_t$.

**What the two copies buy.** They give the two-sided operators for free: an operator $X\mapsto AXB$ is $L_AR_B$, and the whole of $\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{spl}})$ is spanned by the sixteen products $L_{e_\mu}R_{e_\nu}$. The companion article develops that span, its cone of single products and its length; here only the two one-sided families are needed.

## The Product

**Theorem (multiplicativity).** For all $\tilde q,\tilde p$,

$$
\mathsf{M}_2(\tilde q\tilde p)=\mathsf{M}_2(\tilde q)\,\mathsf{M}_2(\tilde p).
$$

**Proof.** Both sides are bilinear, so it suffices to check the sixteen products of basis elements; the three checks of the previous section do that, and the reversed products follow from them because the matrices are known.

**In coordinates.** Writing $\tilde q=(t,x,y,z)$ and $\tilde p=(t',x',y',z')$ for the coefficient vectors, the product is

$$
\tilde q\tilde p=\bigl(tt'-xx'+yy'+zz'\bigr)e_t
+\bigl(tx'+xt'-yz'+zy'\bigr)\vec e_x
+\bigl(ty'+yt'-xz'+zx'\bigr)\vec e_y
+\bigl(tz'+zt'+xy'-yx'\bigr)\vec e_z .
$$

The four lines carry the whole non-commutativity of the algebra. The scalar line is symmetric in the two factors and has the signature $(+,-,+,+)$ of the norm. The three vector lines are not symmetric: each contains two terms with a plus sign, coming from the scalar part of one factor, and two with a minus sign, coming from the vector parts crossing.

**The image.** The image of $\mathsf{M}_2$ is all of $M_2(\mathbb{R})$. This is the structural difference from the quaternion category, where the image is a proper subspace: for $\mathbb{H}$ inside $M_2(\mathbb{C})$ the image has real dimension four in eight, and the missing four dimensions are the ones a matrix model of the quaternions can never reach. Here nothing is missing, and consequently every matrix statement about a split quaternion is a statement about the algebra and conversely.

**The four corners.** Take the idempotent $\tilde\pi_+=\tfrac12(e_t+\vec e_y)$, its complement $\tilde\pi_-=\tfrac12(e_t-\vec e_y)$, and the four Peirce corners $A_{\epsilon\delta}=\tilde\pi_\epsilon A\tilde\pi_\delta$. In the model they are the four matrix units of the basis of lines $L_\pm=\operatorname{span}(1,\pm1)$, with

$$
\mathsf{M}_2(\tilde\pi_+)=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\mathsf{M}_2(\tilde\pi_-)=\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
$$

$$
\mathsf{M}_2\bigl(\tfrac14(\vec e_x-\vec e_z)\bigr)=\tfrac14\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\qquad
\mathsf{M}_2\bigl(-\tfrac14(\vec e_x+\vec e_z)\bigr)=\tfrac14\begin{pmatrix}1&1\\-1&-1\end{pmatrix}.
$$

The two off-diagonal corners are the matrix units $E_{12}$ and $E_{21}$ of that basis, they are nilpotent, and their vanishing square is the matrix form of the Peirce relations. So the algebra has a full system of matrix units, which the quaternion algebra and the split-biquaternion algebra do not have; that absence is the reason those two categories need a separate discussion of what a matrix model can and cannot show.

**What the product does not preserve.** The model is multiplicative but it is not an isometry for any form used below: the determinant of a product is the product of the determinants, but the trace of a product is not the product of the traces, and the Frobenius inner product of a product is not the product of the Frobenius inner products. Multiplicativity is a statement about the algebra, and the forms of the section on norms are statements about the space.

## The Trace

**Theorem (the trace).** For every split quaternion,

$$
\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t=2\operatorname{Sc}(\tilde q).
$$

**Proof.** The diagonal entries are $q_t-q_z$ and $q_t+q_z$, whose sum is $2q_t$.

**The traceless part.** The trace vanishes exactly on the pure elements, so

$$
\mathsf{M}_2(V)=\mathfrak{sl}_2(\mathbb{R})=\{X\in M_2(\mathbb{R}):\operatorname{tr}X=0\},
$$

the three-dimensional space of traceless matrices, spanned by $J$, $K$ and $D$. The scalar part is therefore recovered from the matrix as half the trace, and the projection onto the scalar line is $\tilde q\mapsto\tfrac12\operatorname{tr}\mathsf{M}_2(\tilde q)\,e_t$.

**What the trace sees and does not see.** The trace is insensitive to the sign of the vector part, and it cannot separate a zero divisor from a unit: $\operatorname{tr}\mathsf{M}_2(\vec e_y)=0$ and $\operatorname{tr}\mathsf{M}_2(\vec e_x+\vec e_y)=0$, although the first is a unit of norm $-1$ and the second is a zero divisor of norm $0$. The determinant, below, is the invariant that separates them.

## The Determinant

**Theorem (the determinant).** For every split quaternion,

$$
\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2-q_y^2-q_z^2 .
$$

**Proof.** Expanding the determinant of the dictionary matrix,

$$
(q_t-q_z)(q_t+q_z)-(q_y-q_x)(q_x+q_y)=q_t^2-q_z^2-q_y^2+q_x^2 .
$$

**The signature.** The form $\langle\cdot\rangle_{\natural}$ has signature $(2,2)$: positive on the plane $\operatorname{span}\{e_t,\vec e_x\}$ and negative on $\operatorname{span}\{\vec e_y,\vec e_z\}$. This is the invariant statement that the algebra is $\mathrm{Cl}_{1,1}$ and not $\mathrm{Cl}_{2,0}$, and it is the reason the model has real lightlike directions where a positive definite matrix algebra would have none.

**The three strata.** The rank of the matrix stratifies the algebra,

| condition | stratum | dimension | elements |
|---|---|---|---|
| $\det\neq0$ | units | $4$ | the invertible elements |
| $\det=0$, $\tilde q\neq0$ | zero divisors | $3$ | the rank-one matrices |
| $\tilde q=0$ | the origin | $0$ | the zero matrix |

and the middle stratum is the null cone $\{\langle\tilde q\rangle_{\natural}=0\}\setminus\{0\}$, a cone over a doubly ruled quadric. The rank is the distance from invertibility: rank two exactly on the units, rank one exactly on the nonzero zero divisors.

**Multiplicativity and the unit criterion.** $\det(\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p))=\det\mathsf{M}_2(\tilde q)\det\mathsf{M}_2(\tilde p)$ because the model is multiplicative, and an element is a unit exactly when its matrix is invertible, that is exactly when $\det\neq0$ and $\langle\tilde q\rangle_{\natural}\neq0$. The equivalence is the matrix form of the theorem of *Split-Quaternion Norm and Invertibility*, and it is the reason the algebra has zero divisors at all: the form is indefinite, so it vanishes on a cone and not only at the origin.

**The two rulings.** A rank-one matrix is an outer product $uv^{\mathsf T}$ with $u,v\neq0$, and the pair $(u,v)$ is defined up to a common scalar. The zero divisors are therefore the projectivised pairs,

$$
\{uv^{\mathsf T}\}\;\cong\;\mathbb{P}^1(\mathbb{R})\times\mathbb{P}^1(\mathbb{R}),
$$

the Segre quadric, and its two families of lines are the two rulings. In algebra terms the two rulings are the minimal left ideals and the minimal right ideals, which the section on the projective line develops.

## The Spectral Projectors

**The discriminant.** The characteristic polynomial of $\mathsf{M}_2(\tilde q)$ is $\lambda^2-2q_t\lambda+\langle\tilde q\rangle_{\natural}$, so the discriminant is

$$
\operatorname{tr}^2-4\det=4\bigl(q_y^2+q_z^2-q_x^2\bigr).
$$

The spectral type of the element is decided by the sign of the form $q_y^2+q_z^2-q_x^2$, which is of signature $(2,1)$ on the vector part: this is the form whose light cone is the cone of nilpotent directions.

| sign of $q_y^2+q_z^2-q_x^2$ | eigenvalues | spectrum | centraliser |
|---|---|---|---|
| $>0$ | two distinct reals, $q_t\pm\sqrt{q_y^2+q_z^2-q_x^2}$ | split | $\mathbb{R}\times\mathbb{R}$ |
| $=0$ | the double real $q_t$ | parabolic | the dual numbers |
| $<0$ | the conjugate pair $q_t\pm i\sqrt{q_x^2-q_y^2-q_z^2}$ | complex | $\mathbb{C}$ |

**The projectors.** In the split case, with eigenvalues $\lambda_\pm=q_t\pm r$ and $r=\sqrt{q_y^2+q_z^2-q_x^2}\neq0$, the two spectral projectors are

$$
P_\pm=\frac{\mathsf{M}_2(\tilde q)-\lambda_\mp I}{\lambda_+-\lambda_-},
\qquad
P_+^2=P_+,\quad P_-^2=P_-,\quad P_+P_-=0,\quad P_++P_-=I,
$$

and they are rank-one, of trace one and determinant zero. They are the images of the two idempotents of the algebra constructed by the halving map: if $\tilde\zeta^2=e_t$ then $\tilde\pi=\tfrac12(e_t+\tilde\zeta)$ is idempotent, and every nontrivial idempotent arises this way from a pure root of one, $\tilde\zeta=\vec v$ with $\langle\vec v\rangle_{\natural}=-1$. In the model the condition is $\det P=0$ with $\operatorname{tr}P=1$ and $P^2=P$, which is the same thing.

**The idempotent hyperboloid.** The pure roots of one satisfy $v_x^2-v_y^2-v_z^2=-1$, that is $v_y^2+v_z^2=v_x^2+1$, a connected one-sheeted hyperboloid inside $V$. Its image under the halving map is the connected two-dimensional family of nontrivial idempotents, and the model carries it to the connected family of rank-one projections of trace one.

**The parabolic case.** When $q_y^2+q_z^2=q_x^2$ the eigenvalue is double and the matrix is diagonalisable only when it is scalar. Otherwise it is a nontrivial Jordan block, the algebra contains a nonzero nilpotent commuting with the element, and the centraliser is the algebra of dual numbers. The nilpotent direction is the generator of the light cone of the form $q_y^2+q_z^2-q_x^2$, so the parabolic stratum is a cone and not a hypersurface in the vector part.

**The centraliser.** For a non-scalar element the centraliser is two-dimensional and equals the polynomial algebra $\mathbb{R}[\tilde q]$, the span of $I$ and $\mathsf{M}_2(\tilde q)$. The three spectral types give the three real algebras of dimension two: $\mathbb{R}\times\mathbb{R}$ in the split case, the dual numbers in the parabolic case and $\mathbb{C}$ in the complex case. These are exactly the three real Jordan forms of a $2\times2$ matrix, and the model makes the correspondence literal.

## The Adjugate and the Inverse

**Theorem (the adjugate is the conjugation).** Let $\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ be the conjugation of the algebra. Then

$$
\operatorname{adj}\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde q^{\natural}),
$$

and consequently $\mathsf{M}_2(\tilde q)^{-1}=\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$ on the units.

**Proof.** The adjugate of $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is $\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$, which on the dictionary matrix is $\begin{pmatrix}q_t+q_z&-(q_y-q_x)\\-(q_x+q_y)&q_t-q_z\end{pmatrix}$, and that is the dictionary matrix of $\tilde q^{\natural}$.

**The identity is polynomial.** The relation $\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q^{\natural})=\langle\tilde q\rangle_{\natural}I$ holds for every element, invertible or not, because both sides are polynomial in the four coordinates. On the zero divisors it reads $AB=0$ with $A,B\neq0$, which is the matrix form of the zero-divisor cone.

**The transpose.** The transpose is not the conjugation. On the dictionary matrix,

$$
\mathsf{M}_2(\tilde q)^{\mathsf T}=\mathsf{M}_2\bigl(q_te_t-q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\bigr),
$$

so the transpose corresponds to the linear involution that negates the coefficient of $\vec e_x$ alone and fixes $\vec e_y$ and $\vec e_z$. That involution is an **anti**-automorphism, $\sigma(\tilde q\tilde p)=\sigma(\tilde p)\sigma(\tilde q)$, and not an automorphism, since $\sigma(\vec e_x)\sigma(\vec e_y)=-\vec e_z$ while $\sigma(\vec e_x\vec e_y)=\vec e_z$. The transpose is therefore the model of the reversal, and the three distinguished involutions of the algebra become three different matrix operations: the conjugation is the adjugate, the involution negating $\vec e_x$ is the transpose, and the involution negating all three vectors is the inverse up to the norm.

**The shear of the inverse.** On a unit the inverse is $\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$, and its determinant is $1/\langle\tilde q\rangle_{\natural}$, of either sign. So the units of the algebra form the group $\{X:\det X\neq0\}=GL_2(\mathbb{R})$, and the units of norm one form $SL_2(\mathbb{R})$, the double cover of the identity component of the Lorentz group that *Split-Quaternion Rotations and the Lorentz Group* develops.

## The Norms

**Four forms.** The model carries four natural forms, and only one of them is the determinant.

| form | definition | signature | invariant | positive definite |
|---|---|---|---|---|
| determinant form | $\langle\tilde q\rangle_{\natural}=\det\mathsf{M}_2(\tilde q)$ | $(2,2)$ | under the product | no |
| trace form | $\langle X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(XY)$ | $(3,1)$ | under the product | no |
| Frobenius form | $\langle X,Y\rangle_F=\operatorname{tr}(X^{\mathsf T}Y)$ | $(4,0)$ | under the orthogonal group only | yes |
| Killing form on $\mathfrak{sl}_2$ | $B(X,Y)=4\operatorname{tr}(XY)$ | $(2,1)$ | under the algebra automorphisms | no |

**The trace form.** $\operatorname{tr}(XY)$ is invariant under left and right multiplication by units, because $\operatorname{tr}(AXA^{-1}Y)=\operatorname{tr}(XY)$, and its Gram matrix on the basis $(I,J,K,D)$ is $\operatorname{diag}(2,-2,2,2)$, of signature $(3,1)$. It is not the determinant form: the two differ on the vector part, where the trace form is negative on $\vec e_x$ and positive on $\vec e_y,\vec e_z$, the opposite of the norm.

**The Killing form.** On the traceless part, which is $\mathfrak{sl}_2(\mathbb{R})$, the Killing form of the Lie algebra is $B(X,Y)=4\operatorname{tr}(XY)$, of signature $(2,1)$, negative on $J$ and positive on $K$ and $D$. Its light cone is the cone of nilpotent directions, which is the parabolic stratum of the spectral trichotomy read as a Lie-theoretic object.

**The Frobenius form.** $\operatorname{tr}(X^{\mathsf T}X)=\sum X_{ij}^2$ is positive definite and is the Euclidean structure of $\mathbb{R}^4$ under the vectorisation; it is invariant under conjugation by orthogonal matrices and under nothing else. It is the form a numerical computation uses, and it is not an invariant of the algebra.

**The absence.** There is no form that is both positive definite and multiplicative, and there cannot be: a multiplicative form vanishing only at the origin would make the algebra a division algebra, and the algebra has zero divisors. The signature $(2,2)$ of the determinant is the exact measure of that failure.

## The Subspaces

**The tabulation.** Every subspace of the algebra is a subspace of $M_2(\mathbb{R})$, and the dictionary converts between the two descriptions.

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| scalar line | $q_x=q_y=q_z=0$ | $X=\lambda I$ | $1$ |
| vector part $V$ | $q_t=0$ | $\operatorname{tr}X=0$ | $3$ |
| complex plane | $q_y=q_z=0$ | $X$ commutes with $J$ | $2$ |
| split-complex plane | $q_x=q_z=0$ | $X$ symmetric with equal diagonal entries | $2$ |
| split-complex plane | $q_x=q_y=0$ | $X$ diagonal | $2$ |
| symmetric part | $q_x=0$ | $X=X^{\mathsf T}$ | $3$ |
| skew part | $q_t=q_y=q_z=0$ | $X=-X^{\mathsf T}$ | $1$ |
| centre | $q_x=q_y=q_z=0$ | $X=\lambda I$ | $1$ |

**The two isotropic planes.** The complex plane $\operatorname{span}\{e_t,\vec e_x\}$ is a copy of $\mathbb{C}$ inside the algebra, spanned by $I$ and $J$, and it is the only two-dimensional subalgebra on which the norm is definite. The planes $\operatorname{span}\{e_t,\vec e_y\}$ and $\operatorname{span}\{e_t,\vec e_z\}$ are copies of the split-complex numbers, on which the norm is indefinite and the idempotents live. The model shows the difference at a glance: $J$ is a rotation, $K$ and $D$ are reflections.

**The isotropic lines.** The null cone of the norm meets $V$ in the cone $v_x^2=v_y^2+v_z^2$, of signature $(1,2)$, and the rank-one matrices of the algebra are its projectivisation together with the scalar multiples of the idempotents. The isotropic lines of the algebra are therefore the two rulings of the Segre quadric, and no isotropic line is a subalgebra: the product of two isotropic elements is not isotropic in general.

**The idempotent hyperboloid.** The idempotents other than $0$ and $e_t$ are the halved pure roots of one, $\tfrac12(e_t+\vec v)$ with $\langle\vec v\rangle_{\natural}=-1$, which is the one-sheeted hyperboloid $v_y^2+v_z^2=v_x^2+1$; under the model they are the rank-one projections of trace one. The two standard idempotents, from $\vec v=\pm\vec e_y$, are the projections onto the lines $\operatorname{span}(1,\pm1)$.

## The Projective Line

**The minimal left ideals.** For a nonzero element $\tilde x$ the left ideal $\mathbb{H}_{\mathrm{spl}}\tilde x$ is the set of all left multiples, and it is minimal exactly when $\tilde x$ is a zero divisor. In the model, multiplication on the left by arbitrary matrices gives every matrix whose image lies in the line spanned by the columns of $\mathsf{M}_2(\tilde x)$; so a minimal left ideal is the set of matrices with image in a fixed line,

$$
\mathbb{H}_{\mathrm{spl}}\tilde x=\{X:\operatorname{Im}X\subseteq L\},
$$

and the line $L$ depends only on the ideal. Such a set is two-dimensional, spanned by $u\zeta_1^{\mathsf T}$ and $u\zeta_2^{\mathsf T}$ for a generator $u$ of $L$, so it is a minimal left ideal; the minimal left ideals are therefore parametrised by the lines of $\mathbb{R}^2$, that is by $\mathbb{P}^1(\mathbb{R})$, and the same argument on the right gives the minimal right ideals, parametrised by the lines of the dual, which is again $\mathbb{P}^1(\mathbb{R})$.

**The action.** The units act on the set of minimal left ideals by left multiplication, $g\cdot L=gL$, so the action of ${\mathbb{H}_{\mathrm{spl}}}^{\times}=GL_2(\mathbb{R})$ on $\mathbb{P}^1(\mathbb{R})$ is the defining action on lines. Its kernel is the centre $\mathbb{R}^{\times}I$, because a matrix fixing every line is scalar, so the effective group is

$$
\mathrm{PGL}_2(\mathbb{R})=\operatorname{Aut}(\mathbb{H}_{\mathrm{spl}}),
$$

and the action of the algebra's automorphism group on its minimal left ideals is faithful. This is the geometric content of the previous section's abstract statement that the automorphisms are inner.

**The chart and the Möbius formula.** On the chart $t=\zeta_1/\zeta_2$ of a line $[\zeta]$ with $\zeta_2\neq0$, a matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ acts by

$$
t\longmapsto\frac{at+b}{ct+d},
$$

the Möbius transformation of the projective line, and the point $t=-d/c$ is sent to the line at infinity. The two fixed points of the transformation are the eigendirections of the matrix, which are real in the split case, double in the parabolic case and complex conjugate in the complex case; the trichotomy of the spectral projectors is therefore the trichotomy of Möbius transformations into hyperbolic, parabolic and elliptic.

**The Lorentz reading.** The subgroup $SL_2(\mathbb{R})$ of the units of norm one acts on $\mathbb{P}^1(\mathbb{R})$ through $\mathrm{PGL}_2(\mathbb{R})$, and this action is the action of the identity component of $SO(2,1)$ on the boundary circle of the hyperbolic plane. The three types of Möbius transformation are then the three conjugacy classes of Lorentz transformations in three dimensions, and the null cone of the algebra is the light cone of that group. This is the reason the split-quaternion algebra, and not the quaternion algebra, is the algebra of the Lorentz group in $2+1$ dimensions.

**The cross-ratio.** The action of $\mathrm{PGL}_2(\mathbb{R})$ on $\mathbb{P}^1(\mathbb{R})$ preserves the cross-ratio of four points, and the cross-ratio is the complete invariant of a quadruple under the action. In the algebra, a quadruple of minimal left ideals is a quadruple of zero divisors up to scalar, and the cross-ratio is the invariant that no product and no norm can see.

## Summary

1. The model $\mathsf{M}_2$ is an isomorphism $\mathbb{H}_{\mathrm{spl}}\cong M_2(\mathbb{R})$, unique up to conjugacy, with $\operatorname{Aut}(\mathbb{H}_{\mathrm{spl}})\cong\mathrm{PGL}_2(\mathbb{R})$.
2. The left and right matrices are the two commuting copies $M_{\tilde q}\otimes I$ and $I\otimes M_{\tilde q}^{\mathsf T}$ inside $M_4(\mathbb{R})$, of rank $2\operatorname{rank}M_{\tilde q}$ each.
3. The product is the matrix product, the image is the whole matrix algebra, and the Peirce corners are a full system of matrix units.
4. The trace is twice the scalar part, and the traceless part is $\mathfrak{sl}_2(\mathbb{R})$.
5. The determinant is the norm $\langle\tilde q\rangle_{\natural}$, of signature $(2,2)$; the units are the nonsingular matrices and the zero divisors are the rank-one matrices, that is the Segre quadric.
6. The spectral trichotomy is decided by the sign of $q_y^2+q_z^2-q_x^2$, and the centraliser is $\mathbb{R}\times\mathbb{R}$, the dual numbers or $\mathbb{C}$ accordingly.
7. The conjugation is the adjugate, the transpose is the reversal, and the inverse is the conjugate divided by the norm.
8. Four forms coexist: the determinant form of signature $(2,2)$, the trace form of signature $(3,1)$, the positive definite Frobenius form and the Killing form of signature $(2,1)$.
9. The subspaces are matrix conditions, and the two isotropic planes are the copies of $\mathbb{C}$ and of the split-complex numbers.
10. The minimal left ideals are the lines of $\mathbb{R}^2$, the units act by Möbius transformations, and $\mathrm{PGL}_2(\mathbb{R})$ acts faithfully.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the defining isomorphism $\mathbb{H}_{\mathrm{spl}}\to M_2(\mathbb{R})$ | this article |
| $J,K,D$ | the images of $\vec e_x,\vec e_y,\vec e_z$ | this article |
| $\langle\tilde q\rangle_{\natural}$ | the split-quaternion norm $q_t^2+q_x^2-q_y^2-q_z^2$ | *Split-Quaternion Norm and Invertibility* |
| $\tilde q^{\natural}$ | the conjugation $q_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ | *Split-Quaternion Subspaces and the Involutions* |
| $L_{\tilde q},R_{\tilde q}$ | left and right multiplication, $4\times4$ matrices | this article |
| $\tilde\pi_\pm$ | the idempotents $\tfrac12(e_t\pm\vec e_y)$ | this article |
| $A_{\epsilon\delta}$ | the Peirce corner $\tilde\pi_\epsilon A\tilde\pi_\delta$ | this article |
| $\mathfrak{sl}_2(\mathbb{R})$ | the traceless part $\mathsf{M}_2(V)$ | this article |
| $\mathbb{P}^1(\mathbb{R})$ | the space of lines of $\mathbb{R}^2$, the set of minimal left ideals | this article |
| $E_{ij}$ | the matrix units of $M_2(\mathbb{R})$ | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the matrix units and the classification of the idempotents.
- Thomas Y. Lam, *The Algebraic Theory of Quadratic Forms* (Benjamin, 1973), for the norm of signature $(2,2)$ and the split-quaternion algebra as a Clifford algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ and the Lorentz groups.
- Joseph A. Wolf, *Spaces of Constant Curvature* (Publish or Perish, 1974), for the action of $\mathrm{PGL}_2(\mathbb{R})\cong SO^{+}(2,1)$ on the projective line.
