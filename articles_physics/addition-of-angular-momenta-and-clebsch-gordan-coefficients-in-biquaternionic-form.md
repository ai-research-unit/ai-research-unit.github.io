# __Addition of Angular Momenta and Clebsch–Gordan Coefficients in Biquaternionic Form__

## Introduction

The companion article *Angular Momentum and Spin in Biquaternionic Form* established the angular-momentum algebra inside the biquaternion framework: the commutation relations $[\tilde J_i,\tilde J_j]=i\hbar\epsilon_{ijk}\tilde J_k$, the Casimir $\tilde J^2$, the ladder operators, the spin-$\tfrac12$ realisation $\tilde S_k=\tfrac{\hbar}{2}ie_k$ in $\mathbb{M}_+$, and the observation that two spin-$\tfrac12$ degrees of freedom combine in the tensor-product algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$. That article treated the addition of angular momenta in the case it needed for the hydrogen atom — one spin-$\tfrac12$ coupled to an orbital angular momentum — and recorded the coupling of two algebraic spin factors as a remark.

This article develops that remark into the general machinery. Its subject is the **addition of angular momenta and the Clebsch–Gordan coefficients** as they appear inside the biquaternion framework: the coupled operators, the coupled basis, the decomposition of a tensor product of rotation multiplets, and the explicit coefficients for the two cases the framework itself supports, $\tfrac12\otimes\tfrac12$ and $1\otimes1$.

The distinction between what is algebraic and what is imported runs through everything below and is worth stating at the outset. The Clebsch–Gordan coefficients are pure numbers; they belong to the representation theory of the rotation group and are independent of any particular realisation of the spin operators. What the biquaternion framework supplies is three things: the spin-$\tfrac12$ factor as the fundamental module of $\mathbb{B}$, with its operators $\tilde S_k$ as elements of $\mathbb{M}_+$; the two-factor arena $\mathbb{B}\otimes\mathbb{B}$, in which a composite of two fundamental systems lives; and the identification of the $j=1$ and $j=0$ coupled subspaces with the symmetric and antisymmetric parts of the tensor square, which are canonically defined subspaces of the algebra. What the framework does not supply is a module of any dimension other than two. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple module, so it realises $j=0$ and $j=\tfrac12$ as modules and reaches $j\ge1$ only through tensor products, symmetric powers, or the adjoint action. The coupling of two spin-$\tfrac12$ factors is therefore the central case, and the coupling of two spin-$1$ factors is available only because each spin-$1$ factor is itself built from two fundamental ones.

The article is organised as follows. The next section recalls the angular-momentum algebra and fixes the notation for the coupled problem. The section after that sets up two independent systems inside $\mathbb{B}\otimes\mathbb{B}$ and defines the total operators. Then the Clebsch–Gordan series is stated and its dimension count checked. The two cases are then worked out: $\tfrac12\otimes\tfrac12$, where the coupled projectors are the symmetric and antisymmetric projectors of the tensor square and the coefficients are obtained by a one-line ladder computation; and $1\otimes1$, where the coefficients are tabulated. The following section treats the Clebsch–Gordan transformation as an element of the algebra and identifies the sense in which it is not a product of one-factor transformations. The recursion relations satisfied by the coefficients and the Condon–Shortley phase convention are then recorded, and a closing section separates the algebraic content from the imported content.

## The Angular-Momentum Algebra in Biquaternion Form

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, the cyclic relations $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and $e_je_k=-e_ke_j$ for distinct $j,k\in\{1,2,3\}$. The scalar imaginary $i$ is central, $i^2=-1$. The Hermitian subspace $\mathbb{M}_+$ consists of elements with real scalar part and imaginary vector part.

An angular momentum is a triple of Hermitian elements $\tilde J_1,\tilde J_2,\tilde J_3\in\mathbb{M}_+$ satisfying

$$
[\tilde J_i,\tilde J_j]=i\hbar\,\epsilon_{ijk}\tilde J_k .
$$

The **Casimir** and the **ladder operators** are

$$
\tilde J^2=\sum_{k=1}^{3}\tilde J_k^2,\qquad
\tilde J_\pm=\tilde J_1\pm i\tilde J_2 ,
$$

and they satisfy the standard relations

$$
[\tilde J^2,\tilde J_k]=0,\qquad
[\tilde J_3,\tilde J_\pm]=\pm\hbar\tilde J_\pm,\qquad
[\tilde J_+,\tilde J_-]=2\hbar\tilde J_3 .
$$

The ladder operators are not Hermitian and do not lie in $\mathbb{M}_+$: they satisfy $\tilde J_\pm^\dagger=\tilde J_\mp$, so that $\tilde J_\pm^\dagger\ne\tilde J_\pm$ and $\tilde J_\pm$ lies in the full algebra. The Casimir may be written

$$
\tilde J^2=\tilde J_3^2+\tfrac{1}{2}\left(\tilde J_+\tilde J_-+\tilde J_-\tilde J_+\right).
$$

The simultaneous eigenvectors $|j,m\rangle$ of $\tilde J^2$ and $\tilde J_3$ are defined by

$$
\tilde J^2|j,m\rangle=j(j+1)\hbar^2\,|j,m\rangle,\qquad
\tilde J_3|j,m\rangle=m\hbar\,|j,m\rangle,\qquad m=-j,-j+1,\dots,j,
$$

and the ladder operators act by

$$
\tilde J_\pm|j,m\rangle=\hbar\sqrt{(j\mp m)(j\pm m+1)}\;|j,m\pm1\rangle .
$$

For the fundamental case $j=\tfrac12$ the algebra supplies the operators as algebra elements,

$$
\tilde S_k=\tfrac{\hbar}{2}\,ie_k\in\mathbb{M}_+,
$$

with $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$ following from the quaternion product rule $e_je_k=-\delta_{jk}e_0+\sum_l\epsilon_{jkl}e_l$ together with $i^2=-1$. The ladder combinations are

$$
\tilde S_\pm=\tilde S_1\pm i\tilde S_2=\tfrac{\hbar}{2}\left(ie_1\mp e_2\right),
$$

and they are **nilpotent and null in the norm form**,

$$
\tilde S_\pm^2=0,\qquad N(\tilde S_\pm)=\tilde S_\pm\bar{\tilde S}_\pm=0 ,
$$

so the raising and lowering operators of the fundamental module are zero divisors of $\mathbb{B}$. The Casimir is the central element

$$
\tilde S^2=\tfrac{3\hbar^2}{4}e_0 ,
$$

the value $s(s+1)\hbar^2$ with $s=\tfrac12$. The spin eigenstates are the idempotents $P_\pm(\hat n)=\tfrac12(e_0\pm i\hat n)$, on which $\hat n_k\tilde S_k$ has the eigenvalues $\pm\tfrac{\hbar}{2}$. Under the isomorphism $\Phi$ of the companion articles, $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, and $\tilde S_k$ maps to $\tfrac{\hbar}{2}\sigma_k$.

The material point for what follows is that the fundamental module of $\mathbb{B}$ is two-dimensional, so the operators above are the only spin operators the algebra carries internally. Composite angular momenta require more than one factor of the algebra.

## Coupling Two Independent Systems

Two independent systems are placed on the two factors of the tensor-product algebra

$$
\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C}),
$$

with the two factors acting on the separate slots,

$$
\tilde J_k^{(1)}=\tilde J_k\otimes e_0,\qquad
\tilde J_k^{(2)}=e_0\otimes \tilde J_k .
$$

Because the products act on different slots, the cross-commutators vanish,

$$
[\tilde J_i^{(1)},\tilde J_j^{(2)}]=0 ,
$$

and each factor satisfies its own commutation relations. The **total angular momentum** is the sum

$$
\tilde J_k=\tilde J_k^{(1)}+\tilde J_k^{(2)} ,
$$

which again satisfies $[\tilde J_i,\tilde J_j]=i\hbar\epsilon_{ijk}\tilde J_k$, as a direct computation using the vanishing of the cross-commutators shows. Its Casimir is

$$
\tilde J^2=\tilde J_{(1)}^2+\tilde J_{(2)}^2+2\sum_{k=1}^{3}\tilde J_k^{(1)}\tilde J_k^{(2)} ,
$$

where $\tilde J_{(a)}^2=\sum_k(\tilde J_k^{(a)})^2$. The last term is the **coupling term**; it is the only term that is not a sum of one-factor operators.

The coupled states $|j,m\rangle$ are by definition the simultaneous eigenvectors of $\tilde J^2$ and $\tilde J_3$ in the tensor-product space. The product states $|j_1,m_1\rangle|j_2,m_2\rangle$ are eigenvectors of $\tilde J_3$ with eigenvalue $(m_1+m_2)\hbar$, but not of $\tilde J^2$ unless $j_1=0$ or $j_2=0$; the coupling term mixes them. The change from the product basis, in which $\tilde J_3^{(1)}$ and $\tilde J_3^{(2)}$ are diagonal, to the coupled basis, in which $\tilde J^2$ and $\tilde J_3$ are diagonal, is the Clebsch–Gordan transformation.

For the spin factors the two-factor space is the algebra $\mathbb{B}\otimes\mathbb{B}$ itself. Its trace is the product of the factor traces,

$$
\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\,\mathrm{Tr}_\mathbb{B}(y),\qquad \mathrm{Tr}_\mathbb{B}(e_0)=2,\quad \mathrm{Tr}_\mathbb{B}(e_k)=0 ,
$$

so that $\mathrm{Tr}(e_0\otimes e_0)=4$. A product state is represented by the idempotent

$$
P_{\hat m}\otimes P_{\hat n}
=\tfrac14\left(e_0\otimes e_0+i\hat m_ke_k\otimes e_0+i e_0\otimes\hat n_le_l-\hat m_k\hat n_l\,e_k\otimes e_l\right),
$$

which is Hermitian of trace one; the four product idempotents of the spin-$\tfrac12$ basis are $P_\pm(\hat z)\otimes P_\pm(\hat z)$.

One caution belongs here, because it is the reason the tensor product is an assumption rather than a theorem. For a non-commutative algebra, the tensor product of two left $\mathbb{B}$-modules is not naturally a left $\mathbb{B}$-module; the companion article *Biquaternion Representation Theory* records the point. What does act on $\mathbb{B}\otimes\mathbb{B}$ is the algebra $\mathbb{B}\otimes\mathbb{B}$ itself, together with its diagonal subgroup. The angular momenta $\tilde J_k^{(1)},\tilde J_k^{(2)}$ generate the diagonal copy of the rotation algebra, and the coupled states are multiplets of that diagonal algebra. They are not elements of a $\mathbb{B}$-module. This is the structural reason that higher spins enter the framework through the group rather than through the algebra, and it is taken up again in the closing sections.

## The Clebsch–Gordan Series

Let $V_j$ denote the rotation multiplet of spin $j$, $j\in\tfrac12\mathbb{Z}_{\geq0}$, of complex dimension $2j+1$: the representation carried by $|j,m\rangle$ with $m=-j,\dots,j$, and the irreducible module of highest weight $2j$ in the labelling of the companion article *Biquaternion Representation Theory*. For the polynomial representations of the rotation group the decomposition of a tensor product — the **Clebsch–Gordan series** — is

$$
V_{j_1}\otimes V_{j_2}\;\cong\;\bigoplus_{j=|j_1-j_2|}^{j_1+j_2}V_j ,
$$

the coupled spin running in unit steps from $j_1+j_2$ down to $|j_1-j_2|$. The dimension count is the product of the factor dimensions,

$$
(2j_1+1)(2j_2+1)=\sum_{j=|j_1-j_2|}^{j_1+j_2}(2j+1),
$$

which is the standard sum of consecutive odd integers. For two fundamental multiplets and for two triplets,

$$
\tfrac12\otimes\tfrac12=1\oplus0,\qquad 4=3+1 ,
$$

$$
1\otimes1=2\oplus1\oplus0,\qquad 9=5+3+1 .
$$

This is the Clebsch–Gordan rule of the companion article *Biquaternion Representation Theory*, whose representations of the rotation algebra are the same $V_j$; in its polynomial form the rule is the statement that $V_{1/2}^{\otimes2}\cong V_1\oplus V_0$ and $V_{1/2}^{\otimes3}\cong V_{3/2}\oplus2V_{1/2}$.

The coupled states are the linear combinations

$$
|j,m\rangle=\sum_{m_1+m_2=m}\langle j_1,m_1;j_2,m_2|j,m\rangle\,|j_1,m_1\rangle|j_2,m_2\rangle ,
$$

where the bracket is the **Clebsch–Gordan coefficient**. The coefficients vanish unless $m=m_1+m_2$ and $j$ lies in the range above. They are the matrix elements of the unitary change of basis between the product basis and the coupled basis, and therefore satisfy the orthogonality and completeness relations

$$
\sum_{m_1,m_2}\langle j_1,m_1;j_2,m_2|j,m\rangle\langle j_1,m_1;j_2,m_2|j',m'\rangle=\delta_{jj'}\delta_{mm'} ,
$$

$$
\sum_{j,m}\langle j_1,m_1;j_2,m_2|j,m\rangle\langle j_1,m_1';j_2,m_2'|j,m\rangle=\delta_{m_1m_1'}\delta_{m_2m_2'} .
$$

Both relations are statements about numbers; neither involves the biquaternion realisation. What the realisation enters is the identification of the factor multiplets with the fundamental module and its tensor powers.

The closed expression, Wigner's formula, is

$$
\begin{aligned}
\langle j_1,m_1;j_2,m_2|j,m\rangle
&=\delta_{m,\,m_1+m_2}\,
\sqrt{\frac{(2j+1)\,(j_1+j_2-j)!\,(j_1-j_2+j)!\,(-j_1+j_2+j)!}{(j_1+j_2+j+1)!}}\\[4pt]
&\quad\times\sqrt{(j_1+m_1)!\,(j_1-m_1)!\,(j_2+m_2)!\,(j_2-m_2)!\,(j+m)!\,(j-m)!}\\[4pt]
&\quad\times\sum_k\frac{(-1)^k}{k!\,(j_1+j_2-j-k)!\,(j_1-m_1-k)!\,(j_2+m_2-k)!\,(j-j_2+m_1+k)!\,(j-j_1-m_2+k)!},
\end{aligned}
$$

the sum running over all integers $k$ for which every factorial has a non-negative argument. The formula is quoted here as the standard closed form, not as a biquaternion result; it reproduces every entry of the tables below.

## The Coupling of Two Fundamental Systems

### The coupled states

Take $j_1=j_2=\tfrac12$, so that the product basis is

$$
|\!\uparrow\uparrow\rangle,\quad |\!\uparrow\downarrow\rangle,\quad |\!\downarrow\uparrow\rangle,\quad |\!\downarrow\downarrow\rangle,
$$

with $\tilde S_3$ eigenvalues $+\hbar,0,0,-\hbar$. The Clebsch–Gordan series gives a triplet $j=1$ and a singlet $j=0$,

$$
|1,1\rangle=|\!\uparrow\uparrow\rangle,\qquad
|1,0\rangle=\tfrac{1}{\sqrt2}\left(|\!\uparrow\downarrow\rangle+|\!\downarrow\uparrow\rangle\right),\qquad
|1,-1\rangle=|\!\downarrow\downarrow\rangle,
$$

$$
|0,0\rangle=\tfrac{1}{\sqrt2}\left(|\!\uparrow\downarrow\rangle-|\!\downarrow\uparrow\rangle\right).
$$

The coefficients $\pm\tfrac{1}{\sqrt2}$ are the whole of the $\tfrac12\otimes\tfrac12$ table.

The lowest triplet state is obtained from the highest by the ladder operator $\tilde S_-=\tilde S_-^{(1)}+\tilde S_-^{(2)}$. In the biquaternion realisation $\tilde S_-=\tfrac{\hbar}{2}(ie_1+e_2)$, and with $\Phi(\tilde S_-)=\hbar\sigma_-$ one has $\sigma_-|\!\uparrow\rangle=|\!\downarrow\rangle$ and $\sigma_-|\!\downarrow\rangle=0$. Hence

$$
\tilde S_-|1,1\rangle=\hbar\left(|\!\downarrow\uparrow\rangle+|\!\uparrow\downarrow\rangle\right)=\sqrt{2}\,\hbar\,|1,0\rangle,
$$

which is the relation $\tilde S_-|1,1\rangle=\hbar\sqrt{(1+1)(1-1+1)}|1,0\rangle$ read off from the general formula. The orthogonal combination is the singlet, and $\tilde S_\pm|0,0\rangle=0$ because the rotation-invariant (total-spin-zero) combination is annihilated by both ladder operators.

### The projectors onto the coupled subspaces

The two coupled subspaces are the symmetric and antisymmetric parts of the tensor square. In the algebra $\mathbb{B}\otimes\mathbb{B}$ they are the ranges of the two idempotents

$$
P_{\mathrm{sym}}=\tfrac{1}{4}\left(3\,e_0\otimes e_0-\sum_{k=1}^{3}e_k\otimes e_k\right),\qquad
P_{\mathrm{asym}}=\tfrac{1}{4}\left(e_0\otimes e_0+\sum_{k=1}^{3}e_k\otimes e_k\right).
$$

Both are Hermitian; both are idempotent; they are orthogonal and sum to the identity,

$$
P_{\mathrm{sym}}^2=P_{\mathrm{sym}},\qquad P_{\mathrm{asym}}^2=P_{\mathrm{asym}},\qquad P_{\mathrm{sym}}P_{\mathrm{asym}}=0,\qquad P_{\mathrm{sym}}+P_{\mathrm{asym}}=e_0\otimes e_0 ,
$$

and their traces are $3$ and $1$, the dimensions of the triplet and the singlet:

$$
\mathrm{Tr}(P_{\mathrm{sym}})=3,\qquad \mathrm{Tr}(P_{\mathrm{asym}})=1 .
$$

The antisymmetric projector is the singlet idempotent of the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, written there as $P_{\mathrm{singlet}}=\tfrac14(e_0\otimes e_0+\sum_k e_k\otimes e_k)$; the symmetric projector is its complement, of rank three. The two are the spectral projectors of the **exchange operator**

$$
F=\tfrac{1}{2}\left(e_0\otimes e_0-\sum_{k=1}^{3}e_k\otimes e_k\right),
$$

which satisfies $F^2=e_0\otimes e_0$ and $F^\dagger=F$, and which exchanges the two factors on the product idempotents. Indeed

$$
P_{\mathrm{sym}}=\tfrac{1}{2}\left(e_0\otimes e_0+F\right),\qquad
P_{\mathrm{asym}}=\tfrac{1}{2}\left(e_0\otimes e_0-F\right),
$$

so the coupled projectors of the fundamental coupling are the $\pm1$ spectral projectors of the exchange operator. Under $\Phi\otimes\Phi$ the exchange operator maps to the standard swap, $F\mapsto\tfrac12(I\otimes I+\sum_k\sigma_k\otimes\sigma_k)$, whose action on a product basis vector is $|a\rangle|b\rangle\mapsto|b\rangle|a\rangle$.

### The Casimir and the coupling term

The coupling term of the total Casimir can be evaluated in closed form. With $\tilde S_k^{(1)}\tilde S_k^{(2)}=\tfrac{\hbar^2}{4}(ie_k)\otimes(ie_k)=-\tfrac{\hbar^2}{4}\,e_k\otimes e_k$ and no sum over $k$ on the right,

$$
\sum_{k=1}^{3}\tilde S_k^{(1)}\tilde S_k^{(2)}=-\frac{\hbar^2}{4}\sum_{k=1}^{3}e_k\otimes e_k
=\frac{\hbar^2}{2}F-\frac{\hbar^2}{4}\,e_0\otimes e_0 ,
$$

using $\sum_k e_k\otimes e_k=e_0\otimes e_0-2F$. The coupling term is therefore a **linear combination of the identity and the exchange operator**, which is the algebraic reason that the exchange operator commutes with the total angular momentum:

$$
[\tilde S_k,F]=0,\qquad k=1,2,3 .
$$

The total Casimir is

$$
\tilde S^2=\tfrac{3\hbar^2}{2}e_0\otimes e_0+2\left(\frac{\hbar^2}{2}F-\frac{\hbar^2}{4}e_0\otimes e_0\right)
=\hbar^2\left(e_0\otimes e_0+F\right),
$$

where the central term is the sum of the two one-factor Casimirs, $\tfrac{3\hbar^2}{4}e_0\otimes e_0$ from each factor. Its eigenvalues on the two coupled subspaces follow from the eigenvalues of $F$:

$$
\tilde S^2\big|_{j=1}=2\hbar^2,\qquad \tilde S^2\big|_{j=0}=0 ,
$$

that is, $j(j+1)\hbar^2$ with $j=1$ and $j=0$. The same result is obtained more directly by writing $\tilde S^2=\tfrac12(\tilde S_+\tilde S_-+\tilde S_-\tilde S_+)+\tilde S_3^2$ and acting on the four product states; the two computations agree. In the form of a spectral decomposition,

$$
\tilde S^2=2\hbar^2\,P_{\mathrm{sym}}+0\cdot P_{\mathrm{asym}} ,
$$

which exhibits the coupled projectors as the spectral projectors of the total Casimir and shows that the Clebsch–Gordan transformation is exactly the transformation that diagonalises $\tilde S^2$ and $\tilde S_3$ simultaneously.

## The Clebsch–Gordan Transformation Inside the Algebra

Ordering the product basis as $\left(|\!\uparrow\uparrow\rangle,|\!\uparrow\downarrow\rangle,|\!\downarrow\uparrow\rangle,|\!\downarrow\downarrow\rangle\right)$ and the coupled basis as $\left(|1,1\rangle,|1,0\rangle,|1,-1\rangle,|0,0\rangle\right)$, the coefficients of the previous section assemble into the matrix

$$
U=\begin{pmatrix}
1&0&0&0\\[2pt]
0&\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\[2pt]
0&0&0&1\\[2pt]
0&\tfrac{1}{\sqrt2}&-\tfrac{1}{\sqrt2}&0
\end{pmatrix},
\qquad
U^\dagger U=UU^\dagger=I_4 ,
$$

whose rows are the coupled states and whose columns are the product states. As an element of $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ it is unitary in the matrix sense, $U U^\dagger=e_0\otimes e_0$, and it is a legitimate element of the two-qubit algebra: every $4\times 4$ matrix is.

Two properties of $U$ are worth recording, because they are the algebraic face of the entanglement of the coupled basis.

First, **$U$ is not a product of one-factor unitaries.** The entanglement is visible in its rows: the fourth row is the singlet

$$
|0,0\rangle=\tfrac{1}{\sqrt2}\left(|\!\uparrow\downarrow\rangle-|\!\downarrow\uparrow\rangle\right),
$$

which is maximally entangled in the product basis and is therefore not a product vector, while the rows of a product unitary $\tilde U_1\otimes\tilde U_2$ are the tensor products of the rows of $\tilde U_1$ and of $\tilde U_2$, hence product vectors in every row. No product unitary can have the singlet among its rows, so $U\neq\tilde U_1\otimes\tilde U_2$. Equivalently, the projectors $P_{\mathrm{sym}}$ and $P_{\mathrm{asym}}$ are not of product form. The Clebsch–Gordan transformation of two fundamental systems is therefore not a rotation of one factor; it is a genuinely two-factor transformation.

Second, the local transformations form a proper subgroup. The elements $\tilde U_1\otimes\tilde U_2$ with $\tilde U_a\in\mathbb{B}$ unitary constitute $U(2)\times U(2)$, of real dimension $8$, inside the $U(4)$ of the two-qubit algebra, of real dimension $16$. The Clebsch–Gordan transformation lies in the complement of the local subgroup, in the sense that it changes the entanglement of the basis while preserving the total angular momentum.

The transformation is not unique as a matrix. Only the coupled *projectors* are canonical: the decomposition $\mathbb{C}^4=\mathrm{Sym}^2\oplus\Lambda^2$ is canonical, and within each summand the diagonalisation of $\tilde S_3$ is canonical once the axis is fixed. What remains free is the phase of each coupled state, and it is fixed below by the Condon–Shortley convention. This is the same freedom that appears for any multiplet in the framework: a state is defined up to a central phase $e^{i\alpha}e_0$, and the relative phases of a multiplet are a convention.

## The Coupling of Two Triplets

The second case the framework supports explicitly is $1\otimes1$, where each factor is itself a composite of two fundamental modules. The coupled states therefore live in the four-fold tensor power of the spinor module, on which $\mathbb{B}^{\otimes4}$ acts; equivalently, in the tensor product of the two symmetric squares of the two-qubit subalgebras. The coupled states in the product basis $|m_1\rangle|m_2\rangle$, $m_a\in\{1,0,-1\}$, are

$$
|2,2\rangle=|1\rangle|1\rangle ,
$$

$$
|2,1\rangle=\tfrac{1}{\sqrt2}\left(|1\rangle|0\rangle+|0\rangle|1\rangle\right),
$$

$$
|2,0\rangle=\tfrac{1}{\sqrt6}\left(|1\rangle|\!-\!1\rangle+2\,|0\rangle|0\rangle+|\!-\!1\rangle|1\rangle\right),
$$

$$
|1,1\rangle=\tfrac{1}{\sqrt2}\left(|1\rangle|0\rangle-|0\rangle|1\rangle\right),\qquad
|1,0\rangle=\tfrac{1}{\sqrt2}\left(|1\rangle|\!-\!1\rangle-|\!-\!1\rangle|1\rangle\right),
$$

$$
|1,-1\rangle=\tfrac{1}{\sqrt2}\left(|0\rangle|\!-\!1\rangle-|\!-\!1\rangle|0\rangle\right),\qquad
|0,0\rangle=\tfrac{1}{\sqrt3}\left(|1\rangle|\!-\!1\rangle-|0\rangle|0\rangle+|\!-\!1\rangle|1\rangle\right),
$$

and the states with $m<0$ in the quintet follow by the symmetry $m\to-m$ with the standard phase. The states are simultaneous eigenvectors of the total Casimir and $\tilde S_3$: the quintet carries $j(j+1)=6$, the triplet $2$, the singlet $0$, in units of $\hbar^2$. This is the content of the decomposition $1\otimes1=2\oplus1\oplus0$.

Three features of the table are worth naming. First, the **quintet and the singlet are symmetric** under the exchange of the two factors and the **triplet is antisymmetric**; the symmetry is $(-1)^{j_1+j_2-j}$, so the $j=1$ multiplet obtained from $1\otimes1$ is precisely the antisymmetric combination of the two vector factors, $\Lambda^2V_1\cong V_1$. Second, the singlet is the invariant $\epsilon_{m_1m_2}|m_1\rangle|m_2\rangle$ of the rotation group, and its coefficients are the entries of the alternating form; the same form appears in the two-qubit coupling of the previous section, with the alternating structure realised there by the idempotent $P_{\mathrm{asym}}$. Third, the phases are the Condon–Shortley ones: in every row the coefficient of the largest $m_1$ is positive.

The same construction iterates. In the biquaternion framework a multiplet of spin $s$ is obtained from the $2s$-fold tensor power of the fundamental module as the totally symmetric part, $V_{s}\cong\mathrm{Sym}^{2s}V_{1/2}$, of complex dimension $2s+1$; the completely symmetric projection of $V_{1/2}^{\otimes 2s}$ is the sum of the $2s+1$ totally symmetric idempotents of $(\mathbb{B}\otimes\mathbb{B})^{\otimes s}$, and the coupled states are obtained from the product states by the appropriate coefficients. This is the constructive meaning of the observation that higher spins are reached through symmetric powers rather than as modules.

## The Recursion Relations and the Condon–Shortley Phase

The coefficients are not independent. Applying the raising operator to the definition of $|j,M\rangle$ and reading off the coefficient of $|j_1,m_1\rangle|j_2,m_2\rangle$ with $m_1+m_2=M$ gives, for every $j$ in the range,

$$
\sqrt{(j-M+1)(j+M)}\;\langle j_1,m_1;j_2,m_2|j,M\rangle
=\sqrt{(j_1-m_1+1)(j_1+m_1)}\;\langle j_1,m_1-1;j_2,m_2|j,M-1\rangle
$$
$$
+\sqrt{(j_2-m_2+1)(j_2+m_2)}\;\langle j_1,m_1;j_2,m_2-1|j,M-1\rangle ,
$$

and applying the lowering operator gives the mirror relation

$$
\sqrt{(j+M+1)(j-M)}\;\langle j_1,m_1;j_2,m_2|j,M\rangle
=\sqrt{(j_1+m_1+1)(j_1-m_1)}\;\langle j_1,m_1+1;j_2,m_2|j,M+1\rangle
$$
$$
+\sqrt{(j_2+m_2+1)(j_2-m_2)}\;\langle j_1,m_1;j_2,m_2+1|j,M+1\rangle .
$$

These are the standard recursion relations of the Clebsch–Gordan coefficients, and they are exactly the statement that the coupled states are eigenvectors of the total ladder operators. They determine the whole table once the phase of one state in each multiplet is fixed, which is what makes a phase convention necessary.

The convention used here and throughout the series is the **Condon–Shortley** one: the coefficients are real, and the coefficient of the largest $m_1$ in a coupled state is non-negative. In the two cases above this gives

$$
\langle \tfrac12,\tfrac12;\tfrac12,-\tfrac12|0,0\rangle=+\tfrac{1}{\sqrt2},\qquad
\langle 1,1;1,0|1,1\rangle=+\tfrac{1}{\sqrt2},\qquad
\langle 1,1;1,-1|0,0\rangle=+\tfrac{1}{\sqrt3},
$$

and the signs of the remaining entries follow. The convention has a biquaternion reading: the states of a multiplet are defined up to a central phase $e^{i\alpha}e_0$, and the Condon–Shortley choice is one representative of that phase freedom. The relative signs within a multiplet are then fixed by the requirement that the ladder operators, which are the elements $\tilde S_\pm$ of the algebra, act with the positive square-root coefficients above.

Two consistency checks are worth recording. First, the recursion relations reproduce the closed form of Wigner's formula for $j_1=j_2=1$ in all nine product entries. Second, the recursion is compatible with the orthogonality and completeness relations, as it must be: the recursion is the ladder action in the coupled basis, and the ladder operators are Hermitian conjugates of one another.

## What Is Algebraic and What Is Imported

It is worth stating the accounting explicitly, because the two-spin case is where the framework's reach and its limit are both visible.

**Algebraic.** The two-factor arena $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ and its trace; the total operators $\tilde J_k^{(1)}+\tilde J_k^{(2)}$ and the total Casimir; the coupled projectors $P_{\mathrm{sym}}$ and $P_{\mathrm{asym}}$ as elements of the algebra; the exchange operator $F$ and its relation to the coupling term; the identity of the coupled projectors with the spectral projectors of $\tilde S^2$; the spin-$\tfrac12$ factor with its operators $\tilde S_k\in\mathbb{M}_+$ and the nilpotency $\tilde S_\pm^2=0$. All of these are statements about elements of $\mathbb{B}$ and $\mathbb{B}\otimes\mathbb{B}$ and are consequences of the quaternion product rule, $e_k^2=-e_0$ and $i^2=-1$.

**Imported.** The Clebsch–Gordan coefficients themselves, including their numerical values, their orthogonality and completeness, the recursion relations, the closed Wigner formula, and the Condon–Shortley phase convention. These belong to the representation theory of the rotation group. The framework changes nothing about them; it supplies the objects on which they act.

**Neither.** The identification of $\mathbb{C}^4$ with two spin-$\tfrac12$ systems is an application, not a theorem, of the framework: it presupposes that the tensor product of two fundamental modules is the right description of a composite system, which is the assumption the companion articles leave open. The coupled basis is canonical once that assumption is granted.

The result is a division that is stable across the whole series. Every coefficient of angular-momentum recoupling is imported; every operator that generates the coupling is algebraic; and the structural facts that make the coupling possible — the two-dimensional module, the symmetric and antisymmetric projectors, the exchange operator, the nilpotent ladder operators — are consequences of the algebra.

## Open Questions

Two questions are raised by the accounting above and are not resolved here.

The first is whether the tensor product is canonical for the framework. The two-qubit algebra is used throughout this article, and the coupled projectors are canonical relative to it; but whether the passage from one fundamental module to two is forced by the structure of $\mathbb{B}$, or is one construction among several, is the question the companion articles leave open. A Clebsch–Gordan transformation of two *algebraic* factors would be an additional structural assumption if the tensor product is not natural.

The second is whether a biquaternion construction of the $(2s+1)$-dimensional multiplet exists that is more intrinsic than the symmetric power of the fundamental module. The symmetric power is available and explicit, but it produces a multiplet inside a tensor power of the algebra, not an object of the algebra. Whether the adjoint action, the symmetric powers, and the tensor powers are the only routes to $s\ge1$ inside this framework is precisely the question taken up in the companion problem of the third level, and it is left open here.

## Summary

The addition of angular momenta in the biquaternion framework is the standard coupling of rotation multiplets, carried out on the factors of the tensor-product algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$.

The article established the following.

- **Coupling of two systems.** With $\tilde J_k^{(1)}=\tilde J_k\otimes e_0$ and $\tilde J_k^{(2)}=e_0\otimes\tilde J_k$, the cross-commutators vanish, the total operator $\tilde J_k=\tilde J_k^{(1)}+\tilde J_k^{(2)}$ satisfies the angular-momentum algebra, and the total Casimir is $\tilde J^2=\tilde J_{(1)}^2+\tilde J_{(2)}^2+2\sum_k\tilde J_k^{(1)}\tilde J_k^{(2)}$.
- **Clebsch–Gordan series.** $V_{j_1}\otimes V_{j_2}\cong\bigoplus_{j=|j_1-j_2|}^{j_1+j_2}V_j$, with $(2j_1+1)(2j_2+1)=\sum_j(2j+1)$; in particular $\tfrac12\otimes\tfrac12=1\oplus0$ and $1\otimes1=2\oplus1\oplus0$.
- **The fundamental coupling.** The coupled projectors are the symmetric and antisymmetric projectors of the tensor square,
  $$P_{\mathrm{sym}}=\tfrac14\left(3e_0\otimes e_0-\sum_k e_k\otimes e_k\right),\qquad P_{\mathrm{asym}}=\tfrac14\left(e_0\otimes e_0+\sum_k e_k\otimes e_k\right),$$
  of traces $3$ and $1$; they are the $\pm1$ spectral projectors of the exchange operator $F=\tfrac12(e_0\otimes e_0-\sum_k e_k\otimes e_k)$, and the total Casimir is $\tilde S^2=\hbar^2(e_0\otimes e_0+F)=2\hbar^2P_{\mathrm{sym}}$.
- **The coupling term.** $\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}=\tfrac{\hbar^2}{2}F-\tfrac{\hbar^2}{4}e_0\otimes e_0$, whence $[F,\tilde S_k]=0$: the exchange operator is central in the coupled rotation algebra, which is why it is simultaneously diagonal with the coupled Casimir.
- **The transformation.** The Clebsch–Gordan transformation is the unitary element $U$ of $\mathbb{B}\otimes\mathbb{B}$ that diagonalises $\tilde S^2$ and $\tilde S_3$; it is not a product of one-factor unitaries, since it maps product states to entangled states.
- **The triplet coupling.** For $1\otimes1$ the coupled states carry $j(j+1)=6,2,0$; the quintet is totally symmetric, the singlet totally antisymmetric, and the triplet antisymmetric in the two vector factors.
- **Recursions and phase.** The coefficients satisfy the standard raising and lowering recursions, and the phase is fixed by the Condon–Shortley convention, in which the coefficient of the largest $m_1$ is positive.
- **Division of labour.** The coefficients, their recursion, and their phase convention are imported from the representation theory of the rotation group; the operators that generate the coupling, the projectors, and the exchange operator are elements of the biquaternion algebra and its tensor square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, cyclic products |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$ | Hermitian subspace (observables, states) |
| $\tilde J_k$ | Angular-momentum operators, $[\tilde J_i,\tilde J_j]=i\hbar\epsilon_{ijk}\tilde J_k$ |
| $\tilde J_\pm=\tilde J_1\pm i\tilde J_2$ | Ladder operators |
| $\tilde J^2=\sum_k\tilde J_k^2$ | Casimir |
| $\tilde S_k=\tfrac{\hbar}{2}ie_k$ | Spin-$\tfrac12$ operators in $\mathbb{M}_+$ |
| $\tilde S_\pm=\tfrac{\hbar}{2}(ie_1\mp e_2)$ | Spin ladder operators, $\tilde S_\pm^2=0$ |
| $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ | Two-factor algebra |
| $\tilde J_k^{(1)}=\tilde J_k\otimes e_0,\ \tilde J_k^{(2)}=e_0\otimes\tilde J_k$ | Factor operators |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $V_j$ | Rotation multiplet of spin $j$, highest weight $2j$, $\dim_{\mathbb{C}}V_j=2j+1$ |
| $\langle j_1,m_1;j_2,m_2|j,m\rangle$ | Clebsch–Gordan coefficient (Condon–Shortley phase) |
| $P_{\mathrm{sym}},P_{\mathrm{asym}}$ | Coupled projectors for $\tfrac12\otimes\tfrac12$ |
| $F=\tfrac12(e_0\otimes e_0-\sum_k e_k\otimes e_k)$ | Exchange operator, $F^2=e_0\otimes e_0$ |
| $U$ | Clebsch–Gordan transformation matrix |

## Further Reading

- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the Clebsch–Gordan coefficients, their recursion relations, and the Condon–Shortley phase convention.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton University Press, 1957), for the coupling of angular momenta and the $3j$ formalism.
- E. P. Wigner, *Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra* (Academic Press, 1959), for the closed expression for the Clebsch–Gordan coefficients and the representation-theoretic setting.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the addition of two spin-$\tfrac12$ systems and the standard derivation of the triplet and singlet states.
- Albert Messiah, *Quantum Mechanics* (North-Holland, 1961), for the addition of angular momenta and the transformation between the product and coupled bases.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the Clebsch–Gordan decomposition of $\mathfrak{sl}(2,\mathbb{C})$ representations and the symmetric powers of the defining representation.
- L. C. Biedenharn and J. D. Louck, *Angular Momentum in Quantum Physics* (Addison-Wesley, 1981), for the recoupling theory, the phase conventions, and the general theory of tensor operators.
