# __The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework__

## Introduction

For a two-state system the biquaternion framework gives a complete geometric picture of the state space: the states are the positive, trace-one elements of the Hermitian subspace $\mathbb{M}_+$, and that set is the intersection of the trace-one hyperplane with the future light cone of the norm form. The companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone* establishes this as an exact statement: with

$$
\tilde\rho=\tfrac{1}{2}\left(e_0+i\mathbf r\right),\qquad |\mathbf r|\le 1,
$$

the state space is the closed unit ball, purity is its boundary, and the pure states are at once the idempotents, the extreme rays of the positive cone, and the zero divisors at trace one. The Bloch ball is a canonical object of the algebra because the algebra supplies the cone.

This article asks what survives for spin $1$. The question is well posed because the framework does contain spin-$1$ operators: the adjoint action of the spin algebra on the traceless part of $\mathbb{B}$ is a three-dimensional rotation algebra, and the symmetric sector of $\mathbb{B}\otimes\mathbb{B}$ carries a second realisation. Both give the same spin-$1$ operators, and the companion problem of two spin-$\tfrac12$ particles gives the projectors that select the sector. What does not survive is the cone picture. The state space of a three-level system is eight-dimensional, the positive cone of $\mathbb{M}_+$ is four-dimensional, and no cone of a quadratic form carves out the qutrit state space. The generalisation of the Bloch ball is therefore not another cone slice; it is a genuinely convex eight-dimensional body, and the article's task is to describe it exactly and to say precisely what the algebra does and does not supply.

The results are as follows. The state space of spin $1$ is the face of the two-qubit state space whose support lies in the symmetric subspace, equivalently the positive unit-trace part of the symmetric sector of $\mathbb{B}\otimes\mathbb{B}$. Its states are parametrised by a real eight-vector $\mathbf n$, the **generalized Bloch vector**, normalised here so that the pure states have $|\mathbf n|=1$; the state space is the intersection of the unit ball with the region $\det\rho\ge0$, whose boundary is a cubic hypersurface. The unit ball is necessary but not sufficient, and the largest ball contained in the state space — the **generalized Bloch ball** — has radius exactly $\tfrac{1}{2}$. The pure states form a four-real-dimensional manifold, the complex projective plane $\mathbb{CP}^2$, which is a proper subset of the seven-sphere $|\mathbf n|=1$; the coherent (or classical) states form a two-sphere inside it, and they are exactly the symmetrised products of two fundamental idempotents. A second three-ball, the **polarization ball** $|\langle\mathbf F\rangle|\le1$, is the shadow of the state space on the spin directions; it is not the state space, and confusing the two is the main trap in the geometry of a three-level system.

The article is organised as follows. The next section fixes the qubit result as the reference point. The spin-$1$ operators are then constructed in the framework, both by the adjoint action and by the symmetric combination of two fundamental factors, and the sector in which the states live is identified. The Bloch coordinates are introduced, together with the two invariants that determine the spectrum, and the state space is characterised by the unit ball and the cubic inequality. The inscribed ball of radius $\tfrac{1}{2}$ is then proved to be sharp, the pure states and the coherent states are described, and the two three-balls are compared. A closing section states what the algebra supplies and what it does not.

Throughout, $\hbar=1$ in the geometric formulae, so that the spin-$1$ matrices have eigenvalues $+1,0,-1$; restoring $\hbar$ multiplies every matrix element by $\hbar$.

## The Qubit Bloch Ball as the Reference Point

It is worth stating the reference result in the form that will be generalised. In $\mathbb{M}_+$, an element is written $\tilde H=h_0e_0+i\mathbf h$ with $h_0\in\mathbb{R}$ and $\mathbf h\in\mathbb{R}^3$; its norm form is

$$
N(\tilde H)=h_0^2-|\mathbf h|^2 ,
$$

of signature $(1,3)$, and the positive elements of $\mathbb{M}_+$ are exactly the elements of the closed future cone, $N(\tilde H)\ge0$ with $h_0\ge0$. The trace-one hyperplane is $\mathrm{Sc}(\tilde H)=\tfrac12$, and the states are the intersection of that hyperplane with the cone,

$$
\tilde\rho=\tfrac{1}{2}\left(e_0+i\mathbf r\right),\qquad \mathbf r=2\mathbf h,\qquad |\mathbf r|^2\le1 ,
$$

with eigenvalues $\lambda_\pm=\tfrac12(1\pm|\mathbf r|)$. Purity is the boundary condition $N(\tilde\rho)=\lambda_+\lambda_-=0$, equivalently $|\mathbf r|=1$, equivalently the idempotence of $\tilde\rho$. Three structures coincide on the boundary: the extreme rays of the cone, the rank-one projections, and the zero divisors of $\mathbb{B}$ at trace one.

Three features of this account are the ones that must be examined for spin $1$:

- the state space is a **slice of a cone** by an affine hyperplane;
- the state space is a **ball**, in the Euclidean structure that (minus) the norm form induces on the slice;
- purity is a **quadratic** condition, the vanishing of the norm form.

For spin $1$ the first fails because there is no relevant four-dimensional cone, the second fails because the state space is not a ball, and only the third survives in a weakened form: purity is still the vanishing of a determinant, but the determinant of a $3\times3$ matrix is a cubic, not a quadratic.

## Spin One and Its Operators in the Framework

### The operators

The spin-$1$ operators are constructed in the companion problem of the Wigner–Eckart theorem, by the adjoint action. On the traceless part $W=\operatorname{span}_\mathbb{C}\{ie_1,ie_2,ie_3\}$ of $\mathbb{B}$,

$$
\mathrm{ad}_{\tilde S_k}(ie_l)=[\tilde S_k,ie_l]=i\hbar\,\epsilon_{klm}\,(ie_m),
$$

so that $\tilde J^{(\mathrm{adj})}_k=\mathrm{ad}_{\tilde S_k}$ is an angular momentum in the three-dimensional representation. In the matrix realisation, with $\Phi(e_0)=I_2$ and $\Phi(e_k)=-i\sigma_k$, this is a triple of $3\times3$ matrices acting on $W$ and satisfying

$$
[F_i,F_j]=i\hbar\,\epsilon_{ijk}F_k,\qquad F_1^2+F_2^2+F_3^2=2\hbar^2 I_3 ,
$$

with eigenvalues of each $F_k$ equal to $\hbar$ times $\{+1,0,-1\}$.

A second and equivalent construction uses two fundamental factors,

$$
\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}=\tfrac{\hbar}{2}\left(ie_k\otimes e_0+e_0\otimes ie_k\right),
$$

which is the total spin operator of the two-spin problem. On the three-dimensional symmetric subspace — the range of $P_{\mathrm{sym}}=\tfrac14(3e_0\otimes e_0-\sum_ke_k\otimes e_k)$ — it acts irreducibly as the spin-$1$ operators above, and on the one-dimensional antisymmetric subspace it acts as zero. The two constructions agree; the first exhibits the spin-$1$ operators as the algebra's own inner derivations, the second as a composite of two fundamental systems.

### The sector where the states live

A state of spin $1$ is a positive, unit-trace element of the symmetric sector. In the two-qubit language,

$$
\tilde\rho\ge0,\qquad \mathrm{Tr}_{2Q}(\tilde\rho)=1,\qquad P_{\mathrm{asym}}\,\tilde\rho\,P_{\mathrm{asym}}=0 ,
$$

where $\mathrm{Tr}_{2Q}$ is the trace on $\mathbb{B}\otimes\mathbb{B}$ and $P_{\mathrm{asym}}=\tfrac14(e_0\otimes e_0+\sum_ke_k\otimes e_k)$ is the singlet projector. The last condition says that the support of $\tilde\rho$ lies in the symmetric subspace; the spin-$1$ state space is therefore **the face of the two-qubit state space orthogonal to the antisymmetric projector**. This is the precise sense in which spin-$1$ states are two-qubit states with no singlet component.

For the geometry it is convenient to work in the three-dimensional matrix realisation that $\Phi\otimes\Phi$ provides on the symmetric sector. There the states are the $3\times3$ Hermitian, positive, unit-trace matrices. The framework's Born rule reduces on the sector to $\mathrm{tr}(\rho P)$ for the projector $P$ of a pure state, and observables are the Hermitian $3\times3$ matrices obtained from the symmetric elements of $\mathbb{B}\otimes\mathbb{B}$.

### The spin operators as matrices

In the basis $\{|1,1\rangle,|1,0\rangle,|1,-1\rangle\}$ the spin-$1$ operators are the standard matrices

$$
F_1=\tfrac{1}{\sqrt2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\quad
F_2=\tfrac{1}{\sqrt2}\begin{pmatrix}0&-i&0\\ i&0&-i\\0& i&0\end{pmatrix},\quad
F_3=\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},
$$

which is the realisation used from here on; their matrix elements follow from the algebra elements by the isomorphism, and the commutation relations are those of an angular momentum with $\hbar=1$.

## The State Space of a Three-Level System

### Bloch coordinates and the two invariants

A Hermitian unit-trace $3\times3$ matrix can be written in the Gell-Mann basis $\lambda_1,\dots,\lambda_8$ (traceless, Hermitian, $\mathrm{Tr}(\lambda_a\lambda_b)=2\delta_{ab}$) as

$$
\rho=\tfrac{1}{3}I_3+\frac{1}{\sqrt3}\,n_a\lambda_a,\qquad \mathbf n=(n_1,\dots,n_8)\in\mathbb{R}^8 ,
$$

the **generalized Bloch vector** being $n_a=\tfrac{3\sqrt3}{2}\mathrm{tr}(\rho\lambda_a)$ with $\mathrm{tr}$ the normalised trace, $\mathrm{tr}(I_3)=1$. The normalisation is chosen so that the pure states lie at $|\mathbf n|=1$, matching the qubit convention of the companion article in which the pure states lie at $|\mathbf r|=1$; the standard normalisation of the literature puts the coefficient at $\tfrac12$ instead of $1/\sqrt3$ and the pure states at $|\mathbf n|=2/\sqrt3$, differing by the factor $\sqrt3/2$.

Two invariants determine the spectrum of $\rho$, namely

$$
\mathrm{Tr}(\rho^2)=\tfrac{1}{3}\left(1+2|\mathbf n|^2\right),\qquad \det\rho ,
$$

through the characteristic equation

$$
\lambda^3-\lambda^2+\tfrac{1}{2}\left(1-\mathrm{Tr}(\rho^2)\right)\lambda-\det\rho=0 ,
$$

in which the coefficients use $\mathrm{Tr}\rho=1$. Since the trace is positive, the boundary of positivity is reached when an eigenvalue vanishes, that is, when $\det\rho=0$; and $\mathrm{Tr}(\rho^2)$ fixes the eccentricity of the spectrum about the maximally mixed value $\tfrac13$.

### The necessary condition and the cubic boundary

The spectrum of a positive unit-trace element satisfies $\mathrm{Tr}(\rho^2)\le1$, with equality exactly for the pure states, because $\rho^2\le\rho$ for $0\le\rho\le I$ and the trace is $1$. Hence

$$
|\mathbf n|^2\le1 ,
$$

the **unit-ball condition**, is necessary for every state. It is not sufficient: the determinant can be negative inside the ball. But the two conditions together are exactly the state space.

**Proposition.** *A Hermitian unit-trace matrix $\rho$ is a state if and only if*

$$
|\mathbf n|\le1\qquad\text{and}\qquad \det\rho\ge0 .
$$

*Proof.* Positivity is equivalent to the non-negativity of all three eigenvalues. If $|\mathbf n|\le1$ then $\mathrm{Tr}(\rho^2)\le1$. Suppose an eigenvalue $\lambda_1<0$; then $\det\rho\ge0$ forces $\lambda_2\lambda_3\le0$, and since $\lambda_1\le\lambda_2\le\lambda_3$ and $\lambda_1<0$ the only possibility is $\lambda_2\le0$, whence $\lambda_3=1-\lambda_1-\lambda_2\ge1$ and $\mathrm{Tr}(\rho^2)\ge\lambda_3^2>1$, contradicting $|\mathbf n|\le1$. Thus $\det\rho\ge0$ together with $|\mathbf n|\le1$ forces $\lambda_1\ge0$. The converse is immediate. $\square$

The state space is therefore the intersection of the eight-dimensional unit ball with the region $\det\rho\ge0$, whose boundary is the cubic hypersurface $\det\rho=0$. A numerical scan confirms the structure: along the $\lambda_8$ axis the boundary is at $|\mathbf n|=\tfrac12$ exactly, and the states with $|\mathbf n|>1$ are excluded everywhere.

The cubic is not cosmetic. For the qubit the determinant was a quadratic form, $N(\tilde\rho)=\lambda_+\lambda_-$, and positivity was the single inequality of a Lorentzian cone. For the qutrit the determinant is a cubic and positivity is the conjunction of a quadratic and a cubic inequality; no single quadratic form has the state space as its positivity region. This is the precise sense in which the cone picture does not generalise.

### The spin directions and the quadrupole directions

The eight Bloch directions are not aligned with the physical spin directions. The spin operators are the combinations

$$
F_1=\tfrac{1}{\sqrt2}\left(\lambda_1+\lambda_6\right),\qquad
F_2=\tfrac{1}{\sqrt2}\left(\lambda_2+\lambda_7\right),\qquad
F_3=\tfrac{1}{2}\lambda_3+\tfrac{\sqrt3}{2}\lambda_8 ,
$$

so that the spin vector $\mathbf s=\langle\mathbf F\rangle$ involves the Bloch components

$$
s_1=\sqrt{\tfrac{2}{3}}\left(n_1+n_6\right),\qquad
s_2=\sqrt{\tfrac{2}{3}}\left(n_2+n_7\right),\qquad
s_3=\tfrac{1}{\sqrt3}n_3+n_8 .
$$

The remaining combinations of the eight coordinates describe the quadrupole (alignment) of the state, which has no counterpart for the qubit. Two three-level states can have the same spin vector and different quadrupole, and the geometry of the state space cannot be reconstructed from the spin vector alone. A concrete illustration: the state $\tfrac{1}{\sqrt2}(|1,1\rangle+|1,-1\rangle)$ is pure, so it lies on the boundary $|\mathbf n|=1$, yet its spin vector vanishes, $\langle\mathbf F\rangle=0$; it is a pure state with no polarization along any axis.

## The Inscribed Ball: The Generalized Bloch Ball

The unit ball is the smallest ball containing the state space. The natural generalisation of the Bloch ball is the other extreme: the largest ball contained in it.

**Proposition.** *Every Hermitian unit-trace $\rho$ with $|\mathbf n|\le\tfrac12$ is a state, and the radius $\tfrac12$ is sharp.*

*Proof.* Write $\rho=\tfrac13 I+T$ with $T=\frac{1}{\sqrt3}n_a\lambda_a$ traceless Hermitian, so that $\mathrm{Tr}(T^2)=\tfrac23|\mathbf n|^2$. Let the eigenvalues of $T$ be $\mu_1,\mu_2,\mu_3$; they sum to zero, and their largest value is bounded by

$$
\mu_{\max}\le\sqrt{\tfrac{2}{3}\,\mathrm{Tr}(T^2)}=\tfrac23|\mathbf n| ,
$$

the bound being attained by the spectrum $(\mu_{\max},-\tfrac12\mu_{\max},-\tfrac12\mu_{\max})$. Hence, for any unit vector $|v\rangle$,

$$
\langle v|\rho|v\rangle=\tfrac13+\langle v|T|v\rangle\ge\tfrac13-\mu_{\max}\ge\tfrac13-\tfrac23|\mathbf n|\ge0
\quad\text{whenever } |\mathbf n|\le\tfrac12 ,
$$

so every such $\rho$ is positive, and it is a state. Sharpness: for the direction $\hat n=\lambda_8$ the traceless part has the spectrum $\tfrac{t}{3}(1,1,-2)$, so

$$
\rho=\tfrac{1}{3}I+\tfrac{t}{\sqrt3}\lambda_8
\quad\Longrightarrow\quad
\operatorname{spec}\rho=\left\{\tfrac{1}{3}+\tfrac{t}{3},\ \tfrac{1}{3}+\tfrac{t}{3},\ \tfrac{1}{3}-\tfrac{2t}{3}\right\},
$$

whose least eigenvalue vanishes at $t=\tfrac12$ and is negative for $t>\tfrac12$. The direction $\lambda_8$ therefore reaches the boundary at radius exactly $\tfrac12$, and no ball of larger radius is contained in the state space. $\square$

The radius $r=\tfrac12$ is the standard value for a three-level system. In the normalisation in which the pure states have $|\mathbf n|=1$, the inscribed ball and the pure-state sphere stand in the ratio $\tfrac12$, which is the quantitative statement that the qutrit state space is far from a ball; in the standard normalisation the corresponding radii are $1/\sqrt3$ and $2/\sqrt3$, again in the ratio $\tfrac12$. A numerical search over two thousand random directions in the Bloch space found no boundary closer than $\tfrac12$, consistent with the proposition; the direction that attains it is the $\lambda_8$ direction, whose traceless part has the most eccentric spectrum.

The **generalized Bloch ball** of the spin-$1$ state space is this inscribed ball of radius $\tfrac12$. It is the correct analogue of the qubit Bloch ball in the only sense that can be maintained: every state on it is a state, it is the largest such ball, and its centre is the maximally mixed state $\tfrac13 I_3$. It is not the state space, and it is not the image of any cone slice.

## Pure States, Coherent States, and the Two Three-Balls

### The pure states form $\mathbb{CP}^2$

The pure states are the unit-trace states of rank one. For a positive unit-trace matrix the purity invariant is $\mathrm{Tr}(\rho^2)=\tfrac13(1+2|\mathbf n|^2)$, so $|\mathbf n|=1$ is equivalent to $\mathrm{Tr}(\rho^2)=1$, which for a positive unit-trace matrix is exactly the rank-one condition. Hence, among states,

$$
\rho^2=\rho\iff|\mathbf n|=1\iff\det\rho=0\ \text{with}\ |\mathbf n|=1 .
$$

The set of pure states is therefore the intersection of the unit sphere $S^7$ with the cubic $\det\rho=0$, and it is a four-real-dimensional manifold: the complex projective plane $\mathbb{CP}^2$, of real dimension $4$. Not every point of the unit sphere is a state — those with $\det\rho<0$ satisfy the necessary condition but not the cubic one — and a random point of the sphere is almost never a state, since a four-dimensional manifold has measure zero in a seven-sphere. The dimension count $4<7$ is the reason.

Three strata should be distinguished, and they are the reason the geometry resists a two- or three-dimensional picture.

- **The pure states**: rank one, $|\mathbf n|=1$, forming $\mathbb{CP}^2$, of real dimension $4$. They are the extreme points of the state space.
- **The rank-two boundary**: states with one vanishing eigenvalue, $\det\rho=0$ and $|\mathbf n|<1$; these form the bulk of the boundary of the state space, and are mixed.
- **The interior**: states with all eigenvalues positive, $\det\rho>0$ and $|\mathbf n|<1$; these are invertible and mixed.

The state space is thus an eight-dimensional convex body whose boundary is the union of the pure stratum (dimension $4$) and the rank-two stratum (dimension $7$), cut out by the cubic. For the qubit the corresponding statement collapses: the boundary consists only of the pure states, the sphere $S^2$, because in two dimensions rank one and rank deficiency are the same condition.

### The coherent states

The coherent, or classical, states are the pure states of maximal polarization,

$$
\langle\mathbf F\rangle=\hat n,\qquad |\hat n|=1 ,
$$

and they are obtained from the highest-weight state by the rotation that carries $\hat n_3$ to $\hat n$. In the three-level system they have a closed form in the algebra. With $M=\hat n\cdot\mathbf F$ and $P_0=|1,1\rangle\langle1,1|$,

$$
\rho_{\mathrm{coh}}(\hat n)=\tfrac{1}{2}\left(M^2+M\right),
$$

which is verified to be the projector onto the rotated highest-weight state for every direction; the three eigenvalues of $M$ are $+1,0,-1$ along the $\hat n$ axis, and the numbers $\tfrac12(m^2+m)$, namely $1,0,0$, are the spectral projectors that select $m=+1$.

The coherent states have three equivalent descriptions, and the equivalence is the content of this subsection:

- they are the orbit of the highest-weight idempotent under the adjoint action of the unit quaternions, $P\mapsto\tilde R P\tilde R^\dagger$;
- they are the **symmetrised products of two fundamental idempotents**,
  $$
  \rho_{\mathrm{coh}}(\hat n)=P_{\mathrm{sym}}\left(P_+(\hat n)\otimes P_+(\hat n)\right)P_{\mathrm{sym}},
  $$
  with $P_+(\hat n)=\tfrac12(e_0+i\hat n)$ the qubit idempotent of the companion article; the projection has unit trace and was verified to agree with the closed form for arbitrary directions;
- they are the image of the degree-two Veronese embedding of the Bloch sphere in $\mathbb{CP}^2$.

The last description fixes the topology: the coherent states form a two-sphere $S^2$ inside the four-dimensional pure-state manifold; the map $\hat n\mapsto\rho_{\mathrm{coh}}(\hat n)$ is one-to-one on the Bloch sphere (the phase of the state vector drops out in the projector), and its image is the degree-two Veronese surface in $\mathbb{CP}^2$. The Bloch vector of a coherent state has $|\mathbf n|=1$, so the coherent states lie on the pure-state sphere; but not every pure state is coherent, the obstruction being the dimension count $4>2$.

### The polarization ball is a different three-ball

The spin vector $\mathbf s=\langle\mathbf F\rangle$ has $|\mathbf s|\le1$ for every state. The proof is one line: for any unit vector $\hat n$ the operator $\hat n\cdot\mathbf F$ has eigenvalues $+1,0,-1$, hence $\hat n\cdot\mathbf F\le I$ and

$$
\mathbf s\cdot\hat n=\mathrm{Tr}\left(\rho\,\hat n\cdot\mathbf F\right)\le\mathrm{Tr}(\rho)=1 ,
$$

with equality exactly when $\rho$ is supported on the eigenvalue-$+1$ eigenspace of $\hat n\cdot\mathbf F$, that is, when $\rho=\rho_{\mathrm{coh}}(\hat n)$. Since the map $\rho\mapsto\mathbf s$ is affine and the state space is convex, its image is convex; it contains the origin (the maximally mixed state) and the whole unit sphere (the coherent states), so it is the closed unit ball $|\mathbf s|\le1$, and every vector of length less than one is attained by mixing a coherent state with the maximally mixed state.

This **polarization ball** is a three-ball, but it is not the state space and not the generalized Bloch ball. It is the shadow of the state space on the three spin directions: many states share a spin vector, and the excluded states of the qubit picture reappear here as the states with the same spin vector but different alignment. The two three-balls of the theory are therefore:

| Ball | Definition | What it is |
|---|---|---|
| Generalized Bloch ball | inscribed ball $|\mathbf n|\le\tfrac12$ in the $8$-dimensional Bloch space | a genuine set of states, the largest ball of states |
| Polarization ball | image of the state space under $\rho\mapsto\langle\mathbf F\rangle$ | a three-ball of expectation values, not a set of states |

For the qubit the two coincide, because the Bloch ball is at once the state space, the inscribed ball and the image of the spin directions. For spin $1$ they separate, and this separation is the clearest single statement of what changes between spin $\tfrac12$ and spin $1$.

## What the Algebra Supplies and What It Does Not

**Supplies.** The spin-$1$ operators, as the adjoint action on the traceless part of $\mathbb{B}$ and equivalently as the symmetric combination of two fundamental factors. The sector in which the states live, namely the symmetric face of the two-qubit state space, selected by the projector $P_{\mathrm{sym}}$ of the two-spin problem. The coherent states, as the orbit of a fundamental idempotent, as symmetrised products of two fundamental idempotents, and as the Veronese image of the Bloch sphere. The Born rule, which reduces on the sector to the ordinary trace formula.

**Does not supply.** A cone whose trace-one slice is the state space. The qubit state space was the slice of the future cone of the norm form on $\mathbb{M}_+$ by the hyperplane $\mathrm{Sc}=\tfrac12$; the spin-$1$ state space is eight-dimensional and the positive cone of $\mathbb{M}_+$ is four-dimensional, so no such description is available. Nor is there a single quadratic form whose positivity region is the state space: the determinant of a $3\times3$ matrix is a cubic, and the boundary of the state space is the union of a cubic hypersurface with part of the unit sphere. The qubit's coincidence of positivity, causality, and a quadratic norm form has no spin-$1$ analogue.

**The reason.** This is not an accident of the algebra but a consequence of its module structure. The Hermitian subspace $\mathbb{M}_+$ is the state space of the fundamental module, and the framework's positivity cone is the cone of that module. A three-level system is not a module of $\mathbb{B}$; it is a sector of the tensor square of two fundamental modules, obtained by a projector. The geometry of a projector's range is not the geometry of the algebra's own cone, and the difference is exactly the loss of the ball.

## Summary

The generalized Bloch ball for spin $1$ is the largest ball of states inside the eight-dimensional qutrit state space, and it has radius $\tfrac12$ in the normalisation in which the pure states have $|\mathbf n|=1$.

The article established the following.

- **Spin-one operators.** The adjoint action on the traceless part of $\mathbb{B}$, $\mathrm{ad}_{\tilde S_k}(ie_l)=i\hbar\epsilon_{klm}(ie_m)$, and the symmetric combination $\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ of two fundamental factors give the same spin-$1$ operators, with $[F_i,F_j]=i\hbar\epsilon_{ijk}F_k$ and $\sum_kF_k^2=2\hbar^2I_3$.
- **The state space.** Spin-$1$ states are the positive unit-trace elements of the symmetric sector; in the two-qubit language they are the states whose support lies in the symmetric subspace, $P_{\mathrm{asym}}\tilde\rho P_{\mathrm{asym}}=0$, that is, the face of the two-qubit state space orthogonal to the antisymmetric projector.
- **Bloch coordinates.** $\rho=\tfrac13 I_3+\tfrac{1}{\sqrt3}n_a\lambda_a$ with a real eight-vector $\mathbf n$ normalised so that the pure states have $|\mathbf n|=1$; the spectrum is determined by $\mathrm{Tr}(\rho^2)=\tfrac13(1+2|\mathbf n|^2)$ and $\det\rho$ through the characteristic cubic.
- **The positivity condition.** $\rho$ is a state if and only if $|\mathbf n|\le1$ and $\det\rho\ge0$; the unit ball is necessary, the cubic inequality is what cuts it down, and positivity is no longer a single quadratic condition.
- **The spin directions.** $F_1=\tfrac{1}{\sqrt2}(\lambda_1+\lambda_6)$, $F_2=\tfrac{1}{\sqrt2}(\lambda_2+\lambda_7)$, $F_3=\tfrac12\lambda_3+\tfrac{\sqrt3}{2}\lambda_8$, so the spin vector mixes Bloch coordinates: $s_1=\sqrt{2/3}(n_1+n_6)$, $s_2=\sqrt{2/3}(n_2+n_7)$, $s_3=\tfrac{1}{\sqrt3}n_3+n_8$.
- **The inscribed ball.** Every Hermitian unit-trace $\rho$ with $|\mathbf n|\le\tfrac12$ is a state, and $\tfrac12$ is sharp, attained along $\lambda_8$; the proof uses $\mu_{\max}\le\sqrt{\tfrac23\mathrm{Tr}(T^2)}=\tfrac23|\mathbf n|$ for the traceless part, so that the eigenvalues of $\rho$ are bounded below by $\tfrac13-\tfrac23|\mathbf n|\ge0$ on the ball.
- **Pure and coherent states.** The pure states have $|\mathbf n|=1$ and $\det\rho=0$ and form $\mathbb{CP}^2$, of real dimension $4$; the coherent states have a closed form $\rho_{\mathrm{coh}}(\hat n)=\tfrac12(M^2+M)$ with $M=\hat n\cdot\mathbf F$, satisfy $\langle\mathbf F\rangle=\hat n$, form an $S^2$, and are the symmetrised products of two fundamental idempotents.
- **Two three-balls.** The generalized Bloch ball (radius $\tfrac12$, in the eight-dimensional Bloch space) is a set of states; the polarization ball $|\langle\mathbf F\rangle|\le1$ is its shadow and is not the state space. They coincide only for the qubit.
- **What is lost.** The qubit picture as a cone slice is not available for spin $1$; the state space is not a ball and positivity is not a quadratic condition. The reason is that a three-level system is not a module of $\mathbb{B}$ but a sector of a tensor square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace; positive cone $=$ future cone of $N$ |
| $N(\tilde H)=h_0^2-\lvert\mathbf h\rvert^2$ | Norm form, signature $(1,3)$ |
| $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ | Qubit state, Bloch ball $\lvert\mathbf r\rvert\le1$ |
| $P_{\mathrm{sym}},P_{\mathrm{asym}}$ | Triplet and singlet projectors of $\mathbb{B}\otimes\mathbb{B}$ |
| $F_k$ | Spin-$1$ operators, $[F_i,F_j]=i\hbar\epsilon_{ijk}F_k$ |
| $\mathrm{ad}_{\tilde S_k}$ | Adjoint action on the traceless part $W$ |
| $\lambda_a$, $a=1,\dots,8$ | Gell-Mann basis, $\mathrm{Tr}(\lambda_a\lambda_b)=2\delta_{ab}$ |
| $\rho=\tfrac13I+\tfrac{1}{\sqrt3}n_a\lambda_a$ | Qutrit state, generalized Bloch vector $\mathbf n$ |
| $\mathrm{Tr}(\rho^2)=\tfrac13(1+2\lvert\mathbf n\rvert^2)$ | Purity invariant |
| $\det\rho$ | Cubic invariant; boundary $\det\rho=0$ |
| $\lvert\mathbf n\rvert\le\tfrac12$ | Generalized Bloch ball (inscribed) |
| $\mathbf s=\langle\mathbf F\rangle$, $\lvert\mathbf s\rvert\le1$ | Spin vector; polarization ball |
| $\rho_{\mathrm{coh}}(\hat n)=\tfrac12(M^2+M)$, $M=\hat n\cdot\mathbf F$ | Coherent state |
| $\mathbb{CP}^2$ | Manifold of pure states, real dimension $4$ |

## Further Reading

- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix description of a three-level system and the geometry of the state space.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for the generalized Bloch parametrisation of a qudit and the structure of the state space.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge University Press, 2006), for the convex geometry of the qutrit state space, the inscribed Bloch ball, and the complex projective structure of the pure states.
- G. Kimura, "The Bloch vector for $N$-level systems", *Physics Letters A* 314 (2003) 339, for the parametrisation of the state space by the generalized Bloch vector and the positivity conditions.
- G. Kimura and A. Kossakowski, "The Bloch-vector space for $N$-level systems: the spherical-coordinate system", *Open Systems and Information Dynamics* 12 (2005) 207, for the explicit positivity conditions of the three-level system.
- F. T. Hioe and J. H. Eberly, "$N$-level coherence vector and higher conservation laws in quantum optics", *Physical Review Letters* 47 (1981) 838, for the generalized Bloch vector and the Gell-Mann basis in the physics literature.
- J. M. Radcliffe, "Some properties of coherent spin states", *Journal of Physics A* 4 (1971) 313, for coherent spin states and their relation to classical configurations.
- A. M. Perelomov, *Generalized Coherent States and Their Applications* (Springer, 1986), for the coherent-state manifold, its Veronese embedding, and the orbit construction.
