# __The Wigner–Eckart Theorem and Tensor Operators in Biquaternionic Form__

## Introduction

The coupling of two angular momenta, developed in the companion problem of the addition of angular momenta, is the kinematic half of the theory of rotations. The dynamic half is the classification of operators by how they transform, and the theorem that governs their matrix elements: the Wigner–Eckart theorem. A **tensor operator** of rank $k$ is a family of $2k+1$ operators that rotates as a multiplet of spin $k$; the theorem states that the matrix element of such an operator between two angular-momentum multiplets factorises into a Clebsch–Gordan coefficient, which carries all the dependence on the magnetic quantum numbers, and a single reduced matrix element, which carries all the dynamics.

This article presents that structure in the biquaternion framework. The framework has a distinctive contribution to make at the level of the simplest tensor operators. The **adjoint action** of the spin algebra on $\mathbb{B}$ — the map $x\mapsto[\tilde S_i,x]$ — is a derivation, and on the imaginary quaternion units it reproduces the three-dimensional rotation algebra exactly. The consequence is that the traceless Hermitian part of $\mathbb{B}$ is, under the adjoint action, an irreducible spin-$1$ multiplet: the algebra carries its own rank-$1$ tensor operator, and the split of a Hermitian element into scalar and vector parts is precisely its split into rank-$0$ and rank-$1$ pieces. The spherical components of that vector element turn out to be the ladder operators of the algebra itself.

The rest of the article is the standard theory, honestly labelled as such. The definition of a tensor operator, the Wigner–Eckart theorem, the selection rules, and the reduced-matrix-element technology are imported from the representation theory of the rotation group and are cited as standard. What the framework supplies is the arena — $\mathbb{B}$ and its tensor powers — the rank-$0$ and rank-$1$ tensor operators as algebra elements, the matrix realisation through $\Phi$, and the trace formula that turns the reduced matrix elements into traces. The article therefore follows the pattern of the coupling article: it derives what is algebraic and transcribes what is standard, keeping the two separated.

The article is organised as follows. The next section defines tensor operators and fixes the spherical convention. The section after that works out the adjoint action and exhibits the algebra's own rank-$1$ tensor operator. The Wigner–Eckart theorem is then stated, with the selection rules and the reduced matrix element. Its content is verified explicitly in the coupled two-spin space, where the Clebsch–Gordan coefficients are known, and the reduced matrix elements of the one-particle and total spin operators are computed. Two families of examples follow: vector operators, including the corollary that within a multiplet a vector operator is proportional to the angular momentum, and rank-two operators, including the quadrupole built from the coupling of two vector operators. A short section records the trace form, and a closing section separates the algebraic from the imported content.

## Tensor Operators: Definition and Conventions

An **irreducible tensor operator of rank $k$** is a family $\tilde T^{(k)}_q$, $q=-k,-k+1,\dots,k$, of operators acting on the rotation multiplets, satisfying

$$
[\tilde J_3,\tilde T^{(k)}_q]=\hbar q\,\tilde T^{(k)}_q,\qquad
[\tilde J_\pm,\tilde T^{(k)}_q]=\hbar\sqrt{(k\mp q)(k\pm q+1)}\;\tilde T^{(k)}_{q\pm1},
$$

with $\tilde J_\pm=\tilde J_1\pm i\tilde J_2$ and the square roots vanishing when the target index lies outside the range $-k,\dots,k$. The definition is equivalent to the rotation law

$$
\tilde U(R)\,\tilde T^{(k)}_q\,\tilde U(R)^\dagger
=\sum_{q'=-k}^{k}\mathcal{D}^{(k)}_{q'q}(R)\,\tilde T^{(k)}_{q'},
\qquad
\tilde U(R)=\exp\!\left(-\tfrac{i}{\hbar}\theta\,\hat n_k\tilde J_k\right),
$$

where $\mathcal{D}^{(k)}$ is the $(2k+1)$-dimensional rotation matrix of spin $k$. A **scalar operator** is a rank-$0$ tensor operator, $[\tilde J_k,\tilde T^{(0)}]=0$; a **vector operator** is a rank-$1$ tensor operator, with $[\tilde T_i,\tilde J_j]=i\hbar\epsilon_{ijk}\tilde T_k$ as its defining relation.

The spherical components of a vector operator are fixed by

$$
\tilde T^{(1)}_0=\tilde T_3,\qquad
\tilde T^{(1)}_{\pm1}=\mp\tfrac{1}{\sqrt2}\left(\tilde T_1\pm i\tilde T_2\right),
$$

which satisfies the defining commutators with the minus sign convention displayed above; this is the Condon–Shortley phase convention in its operator form.

Two remarks on the framework belong here. First, a tensor operator need not be an element of $\mathbb{B}$: the definition constrains only the commutators with the angular momenta, and any operator with the right transformation law qualifies, whether it lives in the algebra, in a tensor power of it, or in the module. Second, the rank is not a property of a single operator but of a family; what is characteristic of the framework is how many ranks it can carry inside a single factor, and that question is answered by the adjoint action in the next section.

## The Adjoint Action: The Algebra's Own Tensor Operator

### The derivation

Write a general element of $\mathbb{B}$ in components, $x=x_0e_0+x_ke_k$ with $x_\mu\in\mathbb{C}$; a Hermitian element has $x_0\in\mathbb{R}$ and $x_k=i v_k$ with $v_k\in\mathbb{R}$, so that

$$
\tilde H=h_0e_0+i v_ke_k,\qquad h_0,v_k\in\mathbb{R}.
$$

The **adjoint action** of the spin operators,

$$
\mathrm{ad}_{\tilde S_i}(x)=[\tilde S_i,x]=\tfrac{\hbar}{2}\left[i e_i,x\right],
$$

is a derivation of $\mathbb{B}$: $\mathrm{ad}_{\tilde S_i}(xy)=[\tilde S_i,x]y+x[\tilde S_i,y]$. It is not a left multiplication, and this is the structural difference between the adjoint action and the module action: the algebra acts on its own elements as infinitesimal rotations, not as matrix multiplication on a column.

On the quaternion units the derivation is computed once and for all. Using $[e_i,e_k]=2\epsilon_{ikl}e_l$,

$$
[\tilde S_i,ie_k]=\tfrac{\hbar}{2}\,i\,[e_i,ie_k]=\tfrac{\hbar}{2}\,i\cdot i\,[e_i,e_k]=-\hbar\,\epsilon_{ikl}\,e_l=i\hbar\,\epsilon_{ikl}\,(ie_l),
$$

where the last step uses $e_l=-i\,(ie_l)$. In the basis of imaginary units $ie_k$ of the traceless part this is the defining relation of the three-dimensional rotation representation.

### The rank-one tensor operator of the algebra

The last equation is the statement that the triple

$$
\tilde V_k=ie_k,\qquad k=1,2,3,
$$

is a **vector operator** under the adjoint action, that is, a rank-$1$ irreducible tensor operator with components

$$
(\tilde V)^{(1)}_0=ie_3,\qquad
(\tilde V)^{(1)}_{\pm1}=\mp\tfrac{1}{\sqrt2}\left(ie_1\pm ie_2\right).
$$

Two properties make this operator the natural carrier of the framework's tensor algebra. First, it is built from the generators of the algebra, so it is not an external object: the algebra contains its own vector operator. Second, its spherical components are multiples of the ladder operators,

$$
(\tilde V)^{(1)}_{+1}=-\tfrac{\sqrt2}{\hbar}\,\tilde S_+,\qquad
(\tilde V)^{(1)}_{-1}=+\tfrac{\sqrt2}{\hbar}\,\tilde S_- ,
$$

so the raising and lowering of the adjoint multiplet are generated by the same elements $\tilde S_\pm$ that raise and lower the fundamental module.

The decomposition of a Hermitian element now acquires its meaning,

$$
\tilde H=\underbrace{h_0e_0}_{\text{rank }0}+\underbrace{i v_ke_k}_{\text{rank }1},
$$

and it is invariant under the adjoint action: a rotation acts trivially on the scalar part and by the vector rotation on the vector part,

$$
\tilde H\ \longmapsto\ h_0e_0+i\,(Rv)_k\,e_k ,
$$

with $R\in SO(3)$ the rotation matrix associated with the unit quaternion. This is the same statement as the rotor realisation of rotations in the companion article *Angular Momentum and Spin in Biquaternionic Form*, read as a statement about tensor operators: the adjoint action on $\mathbb{B}$ is the direct sum of a rank-$0$ and a rank-$1$ representation, $\mathbb{B}=\mathbb{C}e_0\oplus W$ with $W\cong V_1$ spanned by $ie_1,ie_2,ie_3$.

The immediate consequence is a **ceiling inside the algebra**. The adjoint action of the spin algebra on $\mathbb{B}$ contains only ranks $0$ and $1$. A tensor operator of rank $k\ge2$ that is an element of a single factor of $\mathbb{B}$ does not exist; rank-$2$ operators require a product of two vector operators, hence a tensor power of the algebra, and the construction is given below. This is the tensor-operator face of the module-theoretic statement that $\mathbb{B}$ has no irreducible representation of dimension greater than two.

## The Wigner–Eckart Theorem

Let $\tilde T^{(k)}_q$ be an irreducible tensor operator of rank $k$, and let $|jm\rangle$ be the angular-momentum multiplets of a rotation-invariant system. Then the **Wigner–Eckart theorem** states that

$$
\langle j'm'|\tilde T^{(k)}_q|jm\rangle
=\langle j,m;k,q|j',m'\rangle\;\langle j'\,\|\tilde T^{(k)}\|\,j\rangle ,
$$

where the first factor is the Clebsch–Gordan coefficient of the coupling $|jm\rangle\otimes|kq\rangle\to|j'm'\rangle$ and the second is the **reduced matrix element**, a number that depends on $j,j',k$ and on the operator but not on $m,m',q$. The conventions are those of the companion problem of the coupling: the Clebsch–Gordan coefficients satisfy the Condon–Shortley phase convention, and the reduced matrix element is defined by the equation above.

The content of the theorem is the factorisation. The dependence on the magnetic quantum numbers is carried entirely by the Clebsch–Gordan coefficient, which is pure geometry; all the dynamics of the operator is compressed into one number per triple $(j',k,j)$. Equivalently: **for fixed $j',k,j$ the ratios**

$$
\frac{\langle j'm'|\tilde T^{(k)}_q|jm\rangle}{\langle j,m;k,q|j',m'\rangle}
\quad\text{(denominator nonzero)}
$$

are equal for every choice of $(m,q,m')$ permitted by the selection rules.

The proof is standard and short. Both sides of the claimed identity satisfy the same recursion relation obtained by commuting the tensor operator with the ladder operators. The recursion determines all the matrix elements of a given $(j',k,j)$ from one of them, and the claimed form satisfies it by construction; the ratio is therefore the same for every allowed triple. Equivalently, the theorem is the statement of Schur's lemma for the intertwining operators of the rotation group. The result is imported here as standard, together with the formal proof; the citations at the end of the article give the derivation.

Two selection rules follow from the Clebsch–Gordan factor and hold independently of the dynamics:

$$
m'=m+q,\qquad
|j-k|\le j'\le j+k ,
$$

the first from the vanishing of the Clebsch–Gordan coefficient unless the magnetic quantum numbers add, the second from the multiplet range of the coupling. For a scalar operator, $k=q=0$ and $\langle j,m;0,0|j',m'\rangle=\delta_{jj'}\delta_{mm'}$, so the theorem reduces to the statement that a scalar operator is diagonal in the multiplets and has one reduced matrix element per $j$ — the content of Schur's lemma for the trivial representation. For a vector operator, $k=1$ and the selection rule is $\Delta j\in\{-1,0,+1\}$ with $m'=m+q$.

## Verification in the Coupled Two-Spin Space

The theorem can be checked against explicit matrices in the two-qubit space, where the coupled multiplets are the triplet $j=1$ and the singlet $j=0$ and the Clebsch–Gordan coefficients are known. The operator used is

$$
\tilde T^{(1)}_q=\tilde S^{(1)}_q ,
$$

the one-particle spin of the first factor, which is a vector operator under the **total** spin because

$$
[\tilde S_i,\tilde S^{(1)}_j]=[\tilde S_i^{(1)},\tilde S^{(1)}_j]=i\hbar\epsilon_{ijk}\tilde S^{(1)}_k .
$$

Its spherical components are those of the previous section applied to the first factor. Working in units $\hbar=1$, forming the matrix elements in the coupled basis, and dividing by the Clebsch–Gordan coefficients, one finds the following.

| $(j',j)$ | permitted $(m,q,m')$ | number of nonzero matrix elements | common ratio | reduced matrix element |
|---|---|---|---|---|
| $(1,1)$ | $q=m'-m$ | $6$ | $+1/\sqrt2$ | $\hbar/\sqrt2$ |
| $(0,1)$ | $m+q=0$ | $3$ | $-\sqrt3/2$ | $-\sqrt3\hbar/2$ |
| $(1,0)$ | $q=m'$ | $3$ | $+1/2$ | $\hbar/2$ |

In every row the ratio is independent of $(m,q,m')$, which is the theorem. The third row uses the trivial coupling coefficient $\langle 0,0;1,q|1,q\rangle=1$.

The same computation for the **total** spin $\tilde T^{(1)}_q=\tilde S_q$ gives a single reduced matrix element,

$$
\langle 1\,\|\tilde S\|\,1\rangle=\sqrt2\,\hbar ,
$$

whose ratio to the one-particle value $\hbar/\sqrt2$ is $2$: the total spin is twice the symmetric part of the one-particle spin, exactly as $\tilde S_q=\tilde S^{(1)}_q+\tilde S^{(2)}_q$ and the two terms contribute equally in the symmetric sector. All three columns are consistent with the theorem and would be impossible if the Clebsch–Gordan factorisation failed.

A last check of the theorem's content is the vanishing of matrix elements that the selection rules permit. For the one-particle operator the $(1,0)$ and $(0,1)$ entries above are nonzero, so no accidental vanishing occurs here; but a rank-$2$ operator built from the same material has no matrix element connecting $j'=1$ to $j=0$, because the triangle condition $|1-2|\le j'\le3$ excludes $j'=0$. The selection rules, not the dynamics, decide which triples can be nonzero.

### A self-contained example: the adjoint multiplet

The two-qubit check uses the tensor product. There is also an example entirely inside a single factor, and it uses the vector operator of the previous section. On the traceless part $W=\mathrm{span}_\mathbb{C}\{ie_1,ie_2,ie_3\}$ the adjoint action is itself the angular momentum of the adjoint representation,

$$
\mathrm{ad}_{\tilde S_k}(ie_l)=[\tilde S_k,ie_l]=i\hbar\,\epsilon_{klm}\,(ie_m),
$$

so that $\tilde J^{(\mathrm{adj})}_k=\mathrm{ad}_{\tilde S_k}$ on $W$ is a spin-$1$ angular momentum. The vector element $ie_k$ acts on $W$ by its own adjoint action, and

$$
\mathrm{ad}_{ie_k}(ie_l)=[ie_k,ie_l]=i^2[e_k,e_l]=-2\epsilon_{klm}e_m=2i\,\epsilon_{klm}(ie_m)
=\frac{2}{\hbar}\,\tilde J^{(\mathrm{adj})}_k(ie_l),
$$

that is, $\mathrm{ad}_{ie_k}=\frac{2}{\hbar}\tilde J^{(\mathrm{adj})}_k$ as operators on $W$. The vector element $ie_k$ is therefore a rank-$1$ tensor operator on $W$, proportional to the angular momentum, and the Wigner–Eckart theorem gives its reduced matrix element with no further input:

$$
\langle 1\|\,\mathrm{ad}_{ie}\,\|1\rangle=\frac{2}{\hbar}\,\langle 1\|\tilde J^{(\mathrm{adj})}\|1\rangle=\frac{2}{\hbar}\cdot\sqrt2\,\hbar=2\sqrt2 .
$$

A direct evaluation in the basis of eigenvectors of $\mathrm{ad}_{\tilde S_3}$, with the spherical components $(\tilde V)^{(1)}_{q}$ of the previous section and the $1\otimes1$ Clebsch–Gordan coefficients, confirms that the ratio of every matrix element to its Clebsch–Gordan coefficient takes the constant value $2\sqrt2$ in the Condon–Shortley $m$-basis of the adjoint multiplet; a different phase convention for the $|m\rangle$ would flip signs while leaving the modulus fixed. This is the framework's own worked example of the theorem: the operator and the multiplet lie inside the algebra and its adjoint action, and only the Clebsch–Gordan coefficients are imported.

## Examples

### Vector operators and the angular-momentum corollary

The simplest vector operator in the framework is the spin itself. On the triplet of the two-spin system the reduced matrix element is $\sqrt2\hbar$, computed above; on the fundamental module of a single factor, $\tilde S^{(1)}_q$ has reduced element $\hbar/\sqrt2$ when regarded as an operator on the coupled space.

A corollary of the theorem covers all vector operators at once. For $k=1$ and $j'=j$, the matrix elements of any two vector operators are proportional to the same Clebsch–Gordan coefficients, so their matrix elements are proportional to one another:

$$
\langle jm'|\tilde V_q|jm\rangle
=c_j\,\langle jm'|\tilde J_q|jm\rangle,
\qquad
c_j=\frac{\langle j\|\tilde V\|j\rangle}{\langle j\|\tilde J\|j\rangle},
$$

with $c_j=\langle j\|\tilde V\|j\rangle/\langle j\|\tilde J\|j\rangle$, where the reduced matrix element of the angular momentum is $\sqrt2\hbar$ on the triplet in the convention used here. This is the operator form of the vector model of the atom: within a multiplet, only the component of a vector operator along $\tilde J$ is effective. For the two-spin system it gives the familiar statement that on the triplet the one-particle spin contributes half of the total, with the transverse components projecting onto $\tilde S$.

### Rank-two operators and the quadrupole

Rank-$2$ tensor operators are built by coupling two rank-$1$ operators with the Clebsch–Gordan coefficients of the coupling $1\otimes1\to2$:

$$
\tilde T^{(2)}_q=\sum_{q_1+q_2=q}\langle 1,q_1;1,q_2|2,q\rangle\,\tilde A_{q_1}\tilde B_{q_2} .
$$

Because the coupling coefficients satisfy the same recursions as the states, the resulting family satisfies the rank-$2$ commutation relations. This was checked explicitly: with $\tilde A=\tilde B=\tilde S^{(1)}$ (the one-particle spherical vector on the two-spin space) and with the $1\otimes1$ coefficients of the companion problem, the five operators $\tilde T^{(2)}_q$, $q=-2,\dots,2$, satisfy

$$
[\tilde S_3,\tilde T^{(2)}_q]=\hbar q\,\tilde T^{(2)}_q,\qquad
[\tilde S_\pm,\tilde T^{(2)}_q]=\hbar\sqrt{(2\mp q)(2\pm q+1)}\,\tilde T^{(2)}_{q\pm1},
$$

as required. The same construction with the total spin $\tilde S$ gives the **quadrupole operator**, whose $q=0$ component is

$$
\tilde T^{(2)}_0=\tfrac{1}{\sqrt6}\left(2\tilde S_0\tilde S_0+\tilde S_{+1}\tilde S_{-1}+\tilde S_{-1}\tilde S_{+1}\right)
=\tfrac{1}{\sqrt6}\left(3\tilde S_3^2-\tilde S^2\right),
$$

using $\tilde S_{+1}\tilde S_{-1}+\tilde S_{-1}\tilde S_{+1}=-(\tilde S_1^2+\tilde S_2^2)$ and $\tilde S_1^2+\tilde S_2^2=\tilde S^2-\tilde S_3^2$, where $\tilde S_q$ denotes the spherical component of order $q$ and $\tilde S_k$ the Cartesian component along axis $k$. On a coherent state pointing at polar angle $\theta$ — an eigenstate of the adjoint rotation with $\langle\mathbf S\rangle=\hat n$ — its expectation is

$$
\langle \hat n|\,\tfrac{1}{\sqrt6}\left(3\tilde S_3^2-\tilde S^2\right)|\hat n\rangle
=\tfrac{1}{\sqrt6}\,P_2(\cos\theta),\qquad
P_2(x)=\tfrac12\left(3x^2-1\right),
$$

which was verified numerically at $\theta=0,\pi/4,\pi/3,\pi/2$ (units $\hbar=1$; restoring $\hbar$ multiplies the expectation by $\hbar^2$). This is the algebraic origin of the quadrupole deformation of a spin-$1$ system: the operator that measures it is the $q=0$ member of the rank-$2$ multiplet built from the spin itself, and its angular dependence is the Legendre polynomial of degree two. The same object reappears as the order parameter of a spin-$1$ condensate.

The general lesson is the one the counting predicts: the product of two rank-$1$ operators decomposes into ranks $2$, $1$ and $0$ according to $1\otimes1=2\oplus1\oplus0$, so the antisymmetric combination gives a rank-$1$ operator and the trace gives a rank-$0$ operator. Higher ranks require longer products; each factor of the product costs one more factor of the algebra, since a single factor carries only ranks $0$ and $1$.

## The Trace Form and the Born Rule

The matrix elements of a tensor operator can be extracted from traces, which is the form in which the framework's Born rule is stated. For a state idempotent $\tilde P$ and an observable $\tilde H$,

$$
\mathrm{Tr}\left(\tilde P\tilde H\right)=2\,\mathrm{Sc}\left(\tilde P\tilde H\right),
$$

the trace formula of the companion articles. A matrix element $\langle j'm'|\tilde T^{(k)}_q|jm\rangle$ is the trace of $\tilde T^{(k)}_q$ against the matrix unit $|jm\rangle\langle j'm'|$, and the reduced matrix element is therefore a trace once a normalisation is chosen. The orthogonality and completeness of the Clebsch–Gordan coefficients used in the theorem are the trace-orthogonality of the coupled projectors of the two-spin problem, written in components.

The trace form has one practical consequence worth stating. Because the reduced matrix element is $m$-independent, it can be extracted from any single nonzero matrix element; the trace formula then gives it as a trace, avoiding the need to fix a basis of the multiplet. In the framework this is the natural way to state the theorem, since $\mathrm{Tr}$ and $\mathrm{Sc}$ are the two invariant pairings the algebra carries, and it keeps the reduction on the algebraic side of the ledger. The price is that the Clebsch–Gordan coefficients remain imported: the trace gives the reduced element, but the geometric factor is still the rotation group's.

## What Is Algebraic and What Is Imported

**Algebraic.** The adjoint action as a derivation; the invariance of the scalar part and the rotation of the vector part; the identification of $ie_k$ as a rank-$1$ tensor operator with spherical components proportional to $\tilde S_\pm$; the decomposition $\mathbb{B}=\mathbb{C}e_0\oplus W$ with $W\cong V_1$; the ceiling that a single factor carries only ranks $0$ and $1$; and the trace form $\mathrm{Tr}(\tilde P\tilde H)=2\mathrm{Sc}(\tilde P\tilde H)$.

**Imported.** The definition of an irreducible tensor operator and its equivalence to the rotation law; the Wigner–Eckart theorem and its proof; the selection rules; the reduced-matrix-element technology; the vector-model corollary; and the Clebsch–Gordan coefficients used to build rank-$2$ operators. These are standard results of the representation theory of the rotation group and are cited as such.

**Neither.** The identification of a physical operator — a magnetic moment, a quadrupole moment, a condensate order parameter — with a particular tensor operator is a modelling choice. The framework supplies the algebra element and the transformation law; which physical quantity it represents is input from the physics.

The pattern is the same as in the two companion problems of coupling and of two spins: the kinematics of the framework is algebraic, the representation theory of the rotation group is imported, and the two meet in the tensor operators that are elements of $\mathbb{B}$ — the scalar and the vector part of a Hermitian element.

## Summary

The Wigner–Eckart theorem in the biquaternion framework is the standard factorisation of the matrix elements of an irreducible tensor operator into a Clebsch–Gordan coefficient and a reduced matrix element, applied to operators that may be elements of $\mathbb{B}$, of its tensor powers, or of the module.

The article established the following.

- **Tensor operators.** An irreducible tensor operator of rank $k$ is a family $\tilde T^{(k)}_q$, $q=-k,\dots,k$, with $[\tilde J_3,\tilde T^{(k)}_q]=\hbar q\tilde T^{(k)}_q$ and $[\tilde J_\pm,\tilde T^{(k)}_q]=\hbar\sqrt{(k\mp q)(k\pm q+1)}\tilde T^{(k)}_{q\pm1}$; a vector operator is the case $k=1$, with spherical components $\tilde T^{(1)}_0=\tilde T_3$, $\tilde T^{(1)}_{\pm1}=\mp\tfrac{1}{\sqrt2}(\tilde T_1\pm i\tilde T_2)$.
- **The algebra's own tensor operator.** The adjoint action $x\mapsto[\tilde S_i,x]$ is a derivation; on the imaginary units $[\tilde S_i,ie_k]=i\hbar\epsilon_{ikl}(ie_l)$, so $\tilde V_k=ie_k$ is a rank-$1$ tensor operator with $(\tilde V)^{(1)}_{\pm1}=\mp\tfrac{\sqrt2}{\hbar}\tilde S_\pm$. A Hermitian element splits as $\tilde H=h_0e_0+iv_ke_k$, a rank-$0$ plus a rank-$1$ piece, and $\mathbb{B}=\mathbb{C}e_0\oplus W$ with $W\cong V_1$ under the adjoint action.
- **The ceiling.** A single factor of $\mathbb{B}$ carries only tensor operators of ranks $0$ and $1$; rank $k\ge2$ requires a product of $k$ vector operators, hence a tensor power of the algebra.
- **The theorem.** $\langle j'm'|\tilde T^{(k)}_q|jm\rangle=\langle j,m;k,q|j',m'\rangle\langle j'\|\tilde T^{(k)}\|j\rangle$, with selection rules $m'=m+q$ and $|j-k|\le j'\le j+k$; for $k=0$ it reduces to Schur's lemma for the trivial representation.
- **Verification.** For the one-particle spin as a vector operator under the total spin, the ratios of matrix elements to Clebsch–Gordan coefficients are $+1/\sqrt2$, $-\sqrt3/2$ and $+1/2$ for $(j',j)=(1,1),(0,1),(1,0)$ in units $\hbar=1$, independent of $(m,q,m')$ in each case; for the total spin on the triplet the reduced matrix element is $\sqrt2\hbar$. For the algebra's own vector operator $ie_k$ acting on the adjoint multiplet $W$, $\mathrm{ad}_{ie_k}=\tfrac{2}{\hbar}\tilde J^{(\mathrm{adj})}_k$ and the reduced matrix element is $2\sqrt2$ (units $\hbar=1$).
- **Examples.** Within a multiplet a vector operator is proportional to $\tilde J$, with the constant fixed by the ratio of reduced matrix elements; coupling two vector operators by the $1\otimes1\to2$ coefficients produces a rank-$2$ tensor operator, whose $q=0$ member for the spin is the quadrupole $\tfrac{1}{\sqrt6}(3\tilde S_3^2-\tilde S^2)$, with coherent-state expectation $\tfrac{1}{\sqrt6}P_2(\cos\theta)$.
- **Trace form.** The Born rule $\mathrm{Tr}(\tilde P\tilde H)=2\mathrm{Sc}(\tilde P\tilde H)$ extracts the reduced matrix elements as traces once a normalisation is chosen, but leaves the Clebsch–Gordan coefficients on the imported side.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde T^{(k)}_q$ | Irreducible tensor operator of rank $k$, component $q$ |
| $\tilde T^{(0)}$ | Scalar operator |
| $\tilde V_q=\tilde T^{(1)}_q$ | Vector operator and its spherical components |
| $[\tilde J_3,\tilde T^{(k)}_q]=\hbar q\tilde T^{(k)}_q$ | Weight condition |
| $[\tilde J_\pm,\tilde T^{(k)}_q]=\hbar\sqrt{(k\mp q)(k\pm q+1)}\tilde T^{(k)}_{q\pm1}$ | Ladder condition |
| $\mathcal{D}^{(k)}_{q'q}(R)$ | Rotation matrix of spin $k$ |
| $\mathrm{ad}_{\tilde S_i}(x)=[\tilde S_i,x]$ | Adjoint action (a derivation) |
| $\tilde V_k=ie_k$ | The algebra's rank-$1$ tensor operator |
| $(\tilde V)^{(1)}_{\pm1}=\mp\tfrac{\sqrt2}{\hbar}\tilde S_\pm$ | Its spherical components |
| $\langle j'm'|\tilde T^{(k)}_q|jm\rangle$ | Matrix element |
| $\langle j'\|\tilde T^{(k)}\|j\rangle$ | Reduced matrix element |
| $\langle j,m;k,q|j',m'\rangle$ | Clebsch–Gordan coefficient (Condon–Shortley) |
| $\mathrm{Tr}(\tilde P\tilde H)=2\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (Born rule) |

## Further Reading

- E. P. Wigner, *Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra* (Academic Press, 1959), for the original statement of the theorem and its representation-theoretic basis.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for tensor operators, the reduced matrix element, and the vector-model corollary.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton University Press, 1957), for the formal proof of the Wigner–Eckart theorem and the selection rules.
- L. C. Biedenharn and J. D. Louck, *Angular Momentum in Quantum Physics* (Addison-Wesley, 1981), for the general theory of tensor operators and the coupling of operators.
- U. Fano and G. Racah, *Irreducible Tensorial Sets* (Academic Press, 1959), for the systematic treatment of irreducible tensor sets and their matrix elements.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the Wigner–Eckart theorem in the form used in atomic and nuclear spectroscopy.
- Albert Messiah, *Quantum Mechanics* (North-Holland, 1961), for tensor operators, the projection theorem, and the applications to multiplets.
