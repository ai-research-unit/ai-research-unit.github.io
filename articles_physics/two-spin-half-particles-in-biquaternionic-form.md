# __Two Spin-Half Particles in Biquaternionic Form__

## Introduction

Two spin-$\tfrac12$ particles form the simplest composite quantum system, and in the biquaternion framework it is also the only composite system that is built without leaving the algebra. Each particle is a fundamental module of $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the pair lives in the tensor-product algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$; and the spin operators of the pair are the sums of the one-particle operators, which are elements of $\mathbb{B}\otimes\mathbb{B}$. Everything the two-particle system does — the triplet and the singlet, the exchange splitting, the Heisenberg coupling, the reduced states — is a statement about elements of that algebra.

This article works out that system. It is the first application of the coupling machinery: the total spin operators, the four coupled states as idempotents of $\mathbb{B}\otimes\mathbb{B}$, the projectors onto the symmetric and antisymmetric subspaces, the exchange operator, the Heisenberg Hamiltonian as an algebra element with its spectrum, and the partial traces of the coupled states. The companion article *Exercise: Two Spins in the Singlet State* computes the singlet alone; the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$* studies the four Bell idempotents; the companion article *Entangled Subsystems in the Biquaternion Framework* fixes the tensor-product arena and the partial traces. This article presents the whole two-spin structure in one place and treats the coupled basis and the Bell basis as two idempotent bases of the same algebra, related by a change of basis.

The division between what is algebraic and what is imported is the same as in the addition of angular momenta. The tensor-product arena, the total operators, the coupled projectors, the exchange operator, and the coupling term are elements of the algebra and follow from the quaternion product rule. The assumption that two particles are described by the tensor product of their state spaces is an assumption, not a theorem of the framework; it is the assumption that makes the rest possible, and it is stated as such. The identifications of the algebra with the standard Pauli-string description of two qubits are consequences of the isomorphism $\Phi$.

The article is organised as follows. The next section fixes the two-qubit algebra, its trace, and its partial traces. Then the total spin operators and their Casimir are constructed, and the coupling term is evaluated in closed form. The four coupled states are exhibited as idempotents, with the projectors onto the symmetric and antisymmetric subspaces. The exchange operator is introduced, its commutation with the total spin proved, and the Heisenberg coupling solved. The partial traces of the coupled states are then computed, and the coupled basis is related to the Bell basis. A closing section states what the composition assumption costs.

## The Two-Qubit Algebra

The arena is the tensor product taken over the complex scalars,

$$
\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C}),
$$

with the bilinear product $(x\otimes y)(x'\otimes y')=xx'\otimes yy'$ and the trace

$$
\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\,\mathrm{Tr}_\mathbb{B}(y),\qquad
\mathrm{Tr}_\mathbb{B}(e_0)=2,\qquad \mathrm{Tr}_\mathbb{B}(e_k)=0 ,
$$

so that $\mathrm{Tr}(e_0\otimes e_0)=4$. Two elements act on different slots,

$$
\tilde S_k^{(1)}=\tilde S_k\otimes e_0,\qquad \tilde S_k^{(2)}=e_0\otimes\tilde S_k ,
$$

and therefore commute with one another,

$$
[\tilde S_i^{(1)},\tilde S_j^{(2)}]=0 .
$$

The isomorphism used throughout sends $e_\mu\otimes e_\nu$ to $\Phi(e_\mu)\otimes\Phi(e_\nu)$ with $\Phi(e_0)=I_2$ and $\Phi(e_k)=-i\sigma_k$; under it $\tilde S_k^{(a)}$ maps to $\tfrac{\hbar}{2}\sigma_k$ acting on the $a$-th factor, and the algebra $\mathbb{B}\otimes\mathbb{B}$ maps onto all of $M_4(\mathbb{C})$.

A state of the pair is a Hermitian, positive, trace-one element of $\mathbb{B}\otimes\mathbb{B}$, and an observable is a Hermitian element. The pure product states are the idempotents

$$
P_{\hat m}\otimes P_{\hat n}=\tfrac{1}{4}\left(e_0\otimes e_0+i\hat m_ke_k\otimes e_0+i e_0\otimes\hat n_le_l-\hat m_k\hat n_l\,e_k\otimes e_l\right),
$$

where $P_{\hat m}=\tfrac12(e_0+i\hat m_ke_k)$ is a one-particle idempotent. The **partial traces** are

$$
\mathrm{Tr}_2(x\otimes y)=x\,\mathrm{Tr}_\mathbb{B}(y),\qquad
\mathrm{Tr}_1(x\otimes y)=y\,\mathrm{Tr}_\mathbb{B}(x),
$$

extended linearly, and they give the reduced states of the two particles.

One structural remark belongs here. The tensor product is the composition rule the framework assumes, not one it derives; the companion articles on biquaternionic quantum mechanics record it among their open questions, and the companion article *Entangled Subsystems in the Biquaternion Framework* uses it directly. Everything below is a statement about $\mathbb{B}\otimes\mathbb{B}$ once that algebra is granted, and the closing section returns to the question.

## The Total Spin Operators

The total spin of the pair is the sum of the one-particle spins,

$$
\tilde S_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}=\tfrac{\hbar}{2}\left(ie_k\otimes e_0+e_0\otimes ie_k\right),
$$

which is a Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$. Because the cross-commutators vanish, the total operators close on the same algebra as one-particle spin:

$$
[\tilde S_i,\tilde S_j]=\tfrac{\hbar^2}{4}\left([ie_i,ie_j]\otimes e_0+e_0\otimes[ie_i,ie_j]\right)=i\hbar\,\epsilon_{ijk}\tilde S_k ,
$$

using $[ie_i,ie_j]=2i\epsilon_{ijk}\,ie_k$, which follows from the quaternion product rule. The total ladder operators are

$$
\tilde S_\pm=\tilde S_1\pm i\tilde S_2=\tilde S_\pm^{(1)}+\tilde S_\pm^{(2)},
\qquad
\tilde S_\pm^{(a)}=\tfrac{\hbar}{2}\left(ie_1\mp e_2\right)\ \text{on the }a\text{-th slot},
$$

and the total Casimir is

$$
\tilde S^2=\sum_{k=1}^{3}\tilde S_k^2
=\left(\tilde S^{(1)}\right)^2+\left(\tilde S^{(2)}\right)^2+2\sum_{k=1}^{3}\tilde S_k^{(1)}\tilde S_k^{(2)} .
$$

The first two terms are central and known: $\left(\tilde S^{(a)}\right)^2=\tfrac{3\hbar^2}{4}e_0\otimes e_0$. The third is the **coupling term**, and it is the only part of $\tilde S^2$ that is not a sum of one-particle operators. It is evaluated in closed form in the next section; it turns out to be a linear combination of the identity and the exchange operator, which is what makes the two-spin system exactly solvable inside the algebra.

## The Coupling Term and the Coupled Projectors

### The coupling term

Each summand of the coupling term factorises in the tensor product,

$$
\tilde S_k^{(1)}\tilde S_k^{(2)}=\tfrac{\hbar^2}{4}\,(ie_k)\otimes(ie_k)=-\tfrac{\hbar^2}{4}\,e_k\otimes e_k ,
$$

with no sum over $k$ on the right, because $(ie_k)^2=e_k^2=-e_0$ implies $(ie_k)\otimes(ie_k)=i^2e_k\otimes e_k=-e_k\otimes e_k$. Summing,

$$
\sum_{k=1}^{3}\tilde S_k^{(1)}\tilde S_k^{(2)}=-\frac{\hbar^2}{4}\sum_{k=1}^{3}e_k\otimes e_k .
$$

The sum $\sum_k e_k\otimes e_k$ is an element of the algebra that is not central but is diagonal in the tensor basis. Defining the **exchange operator**

$$
F=\tfrac{1}{2}\left(e_0\otimes e_0-\sum_{k=1}^{3}e_k\otimes e_k\right),
$$

so that $\sum_k e_k\otimes e_k=e_0\otimes e_0-2F$, the coupling term becomes

$$
\sum_{k=1}^{3}\tilde S_k^{(1)}\tilde S_k^{(2)}=\frac{\hbar^2}{2}\,F-\frac{\hbar^2}{4}\,e_0\otimes e_0 .
$$

The exchange operator is therefore the algebraic carrier of the interaction. Its properties are immediate:

$$
F^2=e_0\otimes e_0,\qquad F^\dagger=F,\qquad \mathrm{Tr}(F)=2,\qquad F\ne \pm e_0\otimes e_0 .
$$

The first follows from $(e_k\otimes e_k)^2=e_k^2\otimes e_k^2=e_0\otimes e_0$ and the orthogonality of the contributions for distinct $k$; the second from $e_k^\dagger=-e_k$; the third from $\mathrm{Tr}(e_k\otimes e_k)=0$. Under $\Phi\otimes\Phi$ the exchange operator becomes $\tfrac12\left(I\otimes I+\sum_k\sigma_k\otimes\sigma_k\right)$, the standard two-qubit swap.

### The coupled projectors

Because $F$ is a Hermitian involution, its spectral projectors are

$$
P_{\mathrm{sym}}=\tfrac{1}{2}\left(e_0\otimes e_0+F\right)=\tfrac{1}{4}\left(3\,e_0\otimes e_0-\sum_{k=1}^{3}e_k\otimes e_k\right),
$$

$$
P_{\mathrm{asym}}=\tfrac{1}{2}\left(e_0\otimes e_0-F\right)=\tfrac{1}{4}\left(e_0\otimes e_0+\sum_{k=1}^{3}e_k\otimes e_k\right).
$$

They are Hermitian idempotents, orthogonal, and complete:

$$
P_{\mathrm{sym}}^2=P_{\mathrm{sym}},\quad P_{\mathrm{asym}}^2=P_{\mathrm{asym}},\quad
P_{\mathrm{sym}}P_{\mathrm{asym}}=0,\quad P_{\mathrm{sym}}+P_{\mathrm{asym}}=e_0\otimes e_0 ,
$$

with traces $3$ and $1$ and trace-orthonormality $\mathrm{Tr}(P_{\mathrm{sym}}P_{\mathrm{asym}})=0$. They are the projectors onto the symmetric and antisymmetric parts of the tensor square of the fundamental module, that is, onto the $j=1$ and $j=0$ coupled subspaces. The antisymmetric projector is the singlet idempotent of the companion article *Exercise: Two Spins in the Singlet State*, written there as $P_{\mathrm{singlet}}$.

The total Casimir now follows in closed form. Substituting the coupling term,

$$
\tilde S^2=\tfrac{3\hbar^2}{2}\,e_0\otimes e_0+2\left(\frac{\hbar^2}{2}F-\frac{\hbar^2}{4}e_0\otimes e_0\right)
=\hbar^2\left(e_0\otimes e_0+F\right),
$$

the central term being the sum of the two one-factor Casimirs $\left(\tilde S^{(a)}\right)^2=\tfrac{3\hbar^2}{4}e_0\otimes e_0$; equivalently, since $e_0\otimes e_0+F=2P_{\mathrm{sym}}$,

$$
\tilde S^2=2\hbar^2P_{\mathrm{sym}}+0\cdot P_{\mathrm{asym}} .
$$

The coupled projectors are exactly the spectral projectors of the total Casimir. This is why the coupling problem of two fundamental modules closes algebraically: the interaction term, the Casimir, and the projectors are all functions of the single element $F$.

## The Four Coupled States as Idempotents

The spectral decomposition of $F$ has two eigenvalues, $+1$ on the triplet and $-1$ on the singlet. To separate the triplet into its three states one diagonalises $\tilde S_3$ within the symmetric subspace, whose spectral projectors are $P_+\otimes P_+$, $P_-\otimes P_-$, and their complement in $P_{\mathrm{sym}}$. With

$$
P_\pm=P_\pm(\hat z)=\tfrac{1}{2}\left(e_0\pm ie_3\right),
$$

the four coupled idempotents are

$$
E_{1,1}=P_+\otimes P_+,\qquad
E_{1,-1}=P_-\otimes P_-,\qquad
E_{1,0}=P_{\mathrm{sym}}-E_{1,1}-E_{1,-1},\qquad
E_{0,0}=P_{\mathrm{asym}} .
$$

Each is a Hermitian idempotent of trace one, they are mutually orthogonal, and they resolve the identity:

$$
E_{j,m}E_{j',m'}=\delta_{jj'}\delta_{mm'}E_{j,m},\qquad
\sum_{j,m}E_{j,m}=e_0\otimes e_0 .
$$

Explicitly, in the tensor basis,

$$
E_{1,1}=\tfrac14\left(e_0\otimes e_0+ie_3\otimes e_0+ie_0\otimes e_3-e_3\otimes e_3\right),
\qquad
E_{1,-1}=\tfrac14\left(e_0\otimes e_0-ie_3\otimes e_0-ie_0\otimes e_3-e_3\otimes e_3\right),
$$

while the two remaining members are of diagonal form,

$$
E_{1,0}=\tfrac{1}{4}\left(e_0\otimes e_0-e_1\otimes e_1-e_2\otimes e_2+e_3\otimes e_3\right),
$$

$$
E_{0,0}=\tfrac{1}{4}\left(e_0\otimes e_0+e_1\otimes e_1+e_2\otimes e_2+e_3\otimes e_3\right).
$$

The two are of the diagonal form $\tfrac14\sum_\mu\epsilon_\mu e_\mu\otimes e_\mu$ with $\epsilon_0=1$ and $\epsilon_1\epsilon_2\epsilon_3=+1$: they are two of the four Bell idempotents of the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, namely those with $\epsilon=(-1,-1,+1)$ and $\epsilon=(+1,+1,+1)$. The states $E_{1,\pm1}$ are single product idempotents and are not of diagonal form. The coupled basis and the Bell basis are two idempotent bases of the same algebra and are related by a Hadamard change of basis, discussed below.

The action of the total spin operators is the expected one. On the projectors the diagonal operators act by multiplication,

$$
\tilde S_3E_{j,m}=m\hbar\,E_{j,m},\qquad
\tilde S^2E_{j,m}=j(j+1)\hbar^2E_{j,m},\qquad
\tilde S_\pm P_{\mathrm{asym}}=0 ,
$$

while the ladder operators move between the states, $E_{j,m}$ being the projector onto $|j,m\rangle$:

$$
\tilde S_+|1,-1\rangle=\hbar\sqrt2\,|1,0\rangle,\qquad
\tilde S_+|1,0\rangle=\hbar\sqrt2\,|1,1\rangle,\qquad
\tilde S_+|1,1\rangle=0,\qquad
\tilde S_\pm|0,0\rangle=0 ,
$$

which is the standard triplet ladder in algebraic form. The last relation is the algebraic statement that the singlet is annihilated by the total ladder operators.

## The Exchange Operator and the Antisymmetry of the Singlet

The exchange operator exchanges the two factors. On a product idempotent,

$$
F\,(P_{\hat m}\otimes P_{\hat n})F=P_{\hat n}\otimes P_{\hat m},
$$

and on the product basis vectors, under $\Phi\otimes\Phi$, it acts as the swap $|a\rangle|b\rangle\mapsto|b\rangle|a\rangle$. It therefore commutes with the total spin operators,

$$
[F,\tilde S_k]=0,\qquad k=1,2,3 ,
$$

which is immediate from the closed form of the coupling term and which can also be verified directly from $F=\tfrac12(e_0\otimes e_0-\sum_ke_k\otimes e_k)$ using the quaternion product rule. The exchange operator is thus a **central element of the coupled rotation algebra**: it commutes with $\tilde S_1,\tilde S_2,\tilde S_3$ and hence with every function of them, in particular with $\tilde S^2$. The commutation is the algebraic reason that the exchange quantum number and the total spin are simultaneously diagonal.

The singlet is antisymmetric under exchange and the triplet members are symmetric:

$$
F\,P_{\mathrm{asym}}=-P_{\mathrm{asym}},\qquad F\,P_{\mathrm{sym}}=+P_{\mathrm{sym}},\qquad
F\,E_{j,m}=(-1)^{1-j}E_{j,m} .
$$

The factor $(-1)^{1-j}$ is the two-particle instance of the general rule $(-1)^{j_1+j_2-j}$ for the exchange symmetry of a coupled multiplet: for two spin-$\tfrac12$ objects the singlet is antisymmetric, and this is what makes it the unique state of vanishing total spin.

Two further algebraic properties of the coupled idempotents are worth recording, because they connect the exchange structure to the zero divisors of the algebra. The ladder operators are nilpotent, and the idempotents they connect are zero divisors of $\mathbb{B}\otimes\mathbb{B}$: for any two distinct coupled idempotents $E,E'$ one has $E\,E'=0$ with both factors nonzero, so each is a zero divisor, and the singlet $P_{\mathrm{asym}}$ in particular satisfies $P_{\mathrm{asym}}(e_0\otimes e_0-P_{\mathrm{asym}})=0$. The singlet is at once the antisymmetric projector, the state of vanishing total spin, and a zero divisor of the two-qubit algebra.

## The Heisenberg Coupling

The exchange structure determines the spectrum of any two-particle interaction built from the total spin. The **Heisenberg coupling** is

$$
\tilde H=-J\sum_{k=1}^{3}\tilde S_k^{(1)}\tilde S_k^{(2)},
\qquad J\ \text{the exchange constant},
$$

the standard isotropic exchange; written in the algebra, using the coupling term,

$$
\tilde H=-J\left(\frac{\hbar^2}{2}F-\frac{\hbar^2}{4}e_0\otimes e_0\right)
=-\frac{J\hbar^2}{2}\,F+\frac{J\hbar^2}{4}\,e_0\otimes e_0 .
$$

This is a Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$ — a legitimate observable — and its spectral decomposition is immediate from that of $F$, on using $F=P_{\mathrm{sym}}-P_{\mathrm{asym}}$ and $e_0\otimes e_0=P_{\mathrm{sym}}+P_{\mathrm{asym}}$:

$$
\tilde H=-\frac{J\hbar^2}{2}\left(P_{\mathrm{sym}}-P_{\mathrm{asym}}\right)+\frac{J\hbar^2}{4}\left(P_{\mathrm{sym}}+P_{\mathrm{asym}}\right)
=-\frac{J\hbar^2}{4}\,P_{\mathrm{sym}}+\frac{3J\hbar^2}{4}\,P_{\mathrm{asym}} .
$$

The eigenvalues are therefore

$$
E_{\text{triplet}}=-\frac{J\hbar^2}{4}\quad\text{(multiplicity 3)},\qquad
E_{\text{singlet}}=+\frac{3J\hbar^2}{4}\quad\text{(multiplicity 1)},
$$

with the **singlet–triplet splitting**

$$
\Delta E=E_{\text{singlet}}-E_{\text{triplet}}=J\hbar^2 .
$$

For $J>0$ the ferromagnetic case the triplet lies lower; for $J<0$ the antiferromagnetic case the singlet lies lower. Both signs are realised in nature — the triplet lies below in the two-electron system of an $s$-band ferromagnet, the singlet below in a molecular antiferromagnet — and the framework's contribution is only to express the Hamiltonian and its spectrum as algebra elements; the sign of $J$ is dynamical input.

The result can be checked without the projector machinery. The eigenvector equation in the form

$$
\tilde S^2=\left(\tilde S^{(1)}+\tilde S^{(2)}\right)^2
=2\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}+\tfrac{3\hbar^2}{2}e_0\otimes e_0
$$

gives $\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}=\tfrac12\left(\tilde S^2-\tfrac{3\hbar^2}{2}e_0\otimes e_0\right)$, so that $\tilde H=-\tfrac{J}{2}\left(\tilde S^2-\tfrac{3\hbar^2}{2}e_0\otimes e_0\right)$ and the eigenvalues are $-\tfrac{J}{2}\left(2\hbar^2-\tfrac{3\hbar^2}{2}\right)=-\tfrac{J\hbar^2}{4}$ on the triplet and $-\tfrac{J}{2}\left(0-\tfrac{3\hbar^2}{2}\right)=+\tfrac{3J\hbar^2}{4}$ on the singlet. The two routes agree.

## Partial Traces and the Reduced States

The coupled states are not all of the same kind, and the partial trace makes the distinction algebraic. For the two outer triplet members, which are product idempotents,

$$
\mathrm{Tr}_2\!\left(E_{1,1}\right)=\mathrm{Tr}_2\!\left(P_+\otimes P_+\right)=P_+\mathrm{Tr}_\mathbb{B}(P_+)=P_+ ,
$$

since $\mathrm{Tr}_\mathbb{B}(P_\pm)=\tfrac{1}{2}\mathrm{Tr}_\mathbb{B}(e_0)=\tfrac12\cdot2=1$. So the reduced state of $E_{1,1}$ is the pure state $P_+$; the same holds for $E_{1,-1}$ with $P_-$.

For the two diagonal-form idempotents the computation is a single line. Because $E_{1,0}$ and $E_{0,0}$ are sums of diagonal tensor terms,

$$
\mathrm{Tr}_2\!\left(E_{1,0}\right)=\tfrac{1}{4}\left(\mathrm{Tr}_\mathbb{B}(e_0)e_0+\sum_{k=1}^{3}\epsilon_k\,\mathrm{Tr}_\mathbb{B}(e_k)e_k\right)=\tfrac{1}{4}\cdot 2\,e_0=\tfrac{1}{2}\,e_0 ,
$$

and likewise $\mathrm{Tr}_2(E_{0,0})=\mathrm{Tr}_1(E_{0,0})=\tfrac12 e_0$ and $\mathrm{Tr}_1(E_{1,0})=\tfrac12 e_0$. The reduced state of both $E_{1,0}$ and $E_{0,0}$ is the **maximally mixed** state of the one-particle system, the centre of the Bloch ball, of purity

$$
\mathrm{Tr}\!\left(\tfrac{1}{2}e_0\cdot\tfrac{1}{2}e_0\right)=\tfrac{1}{4}\mathrm{Tr}_\mathbb{B}(e_0)=\tfrac12 .
$$

The three triplet members therefore fall into two classes: $E_{1,\pm1}$ are product states with pure reduced states, while $E_{1,0}$ is a correlated state with maximally mixed reduced states, exactly like the singlet $E_{0,0}$. The middle triplet state and the singlet share the same reduced data and differ only in their correlations; this is the algebraic content of the statement that the reduced density matrix does not determine the state of a composite. The informational reading of these correlations — their entropy, their discord, their use as a resource — belongs to the informational subcategory and is not taken up here.

## Relation to the Bell Basis

The coupled idempotents and the four Bell idempotents are two orthogonal families of minimal idempotents resolving the identity of $\mathbb{B}\otimes\mathbb{B}$; they are two idempotent bases in the sense of the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, related by a unitary change of basis.

The singlet belongs to both bases: $E_{0,0}=P_{\epsilon}$ with $\epsilon=(+1,+1,+1)$, which is the singlet idempotent $P_{\mathrm{singlet}}$ of the companion articles. The middle triplet member $E_{1,0}$ is the Bell idempotent with $\epsilon=(-1,-1,+1)$, the state $|\Psi^+\rangle$. The two remaining Bell idempotents are the projectors onto the states $\tfrac{1}{\sqrt2}\left(|\!\uparrow\uparrow\rangle\pm|\!\downarrow\downarrow\rangle\right)$, they involve off-diagonal matrix units linking the extreme product states, and are not members of the coupled multiplet.

The two bases are distinguished by what they diagonalise. The coupled basis diagonalises the total Casimir $\tilde S^2$ and the total $\tilde S_3$. The Bell basis diagonalises the two commuting involutions

$$
\sigma_1\otimes\sigma_1,\qquad \sigma_3\otimes\sigma_3 ,
$$

whose four eigenvalue pairs $(s_1,s_3)\in\{\pm1\}^2$ label the four Bell states: $(+,+)$ for $\tfrac{1}{\sqrt2}(|\!\uparrow\uparrow\rangle+|\!\downarrow\downarrow\rangle)$, $(+,-)$ for $\tfrac{1}{\sqrt2}(|\!\uparrow\downarrow\rangle+|\!\downarrow\uparrow\rangle)$, $(-,+)$ for $\tfrac{1}{\sqrt2}(|\!\uparrow\uparrow\rangle-|\!\downarrow\downarrow\rangle)$, and $(-,-)$ for the singlet. Both are complete sets of commuting observables, and they are related by a fixed unitary rotation — the Hadamard transformation on the pair of outer states — which is not a product of one-particle operations, since it maps a product state to a Bell state. The two-spin system therefore carries, already at this level, two inequivalent physical questions — "what is the total spin" and "which Bell state is it" — whose answers are bases of the same algebra.

## The Assumption of Composition

Everything above rests on one assumption that the framework does not derive: that two spin-$\tfrac12$ particles are described by the tensor product $\mathbb{B}\otimes\mathbb{B}$ of their algebras. The algebra is available; the state space $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ with its trace is well defined; the partial traces are natural. But whether the composition of two fundamental systems is *forced* by the structure of $\mathbb{B}$, or is a further postulate, is one of the open questions recorded by the companion articles on biquaternionic quantum mechanics. Nothing in this article depends on the answer, and every statement is a statement about the algebra $\mathbb{B}\otimes\mathbb{B}$ once granted.

Two consequences of the assumption are worth naming because they are structural rather than dynamical. First, the composition rule doubles the module dimension: two fundamental modules give a four-dimensional space, and $n$ of them give $2^n$. The framework therefore composes into powers of two and into nothing else; a three-level system cannot be built from fundamental modules, which is the algebraic ceiling examined in the companion problem of the third level. Second, the local operations — the elements $\tilde U_1\otimes\tilde U_2$ — form a proper subgroup of the unitaries of the composite algebra, so the composite carries a notion of locality that the algebra alone does not supply. Both facts are consequences of the tensor-product assumption as much as of the algebra.

## Summary

Two spin-$\tfrac12$ particles in the biquaternion framework are described by the tensor-product algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$, with total spin operators $\tilde S_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ and partial traces $\mathrm{Tr}_1,\mathrm{Tr}_2$.

The article established the following.

- **Total spin and its Casimir.** $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$, and
  $$\tilde S^2=\hbar^2\left(e_0\otimes e_0+F\right)=2\hbar^2P_{\mathrm{sym}},$$
  where $F=\tfrac12(e_0\otimes e_0-\sum_k e_k\otimes e_k)$ is the exchange operator.
- **The coupling term.** $\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}=\tfrac{\hbar^2}{2}F-\tfrac{\hbar^2}{4}e_0\otimes e_0$, so the interaction between the two spins is carried by the exchange operator; equivalently $[F,\tilde S_k]=0$, whence $F$ is central in the coupled rotation algebra.
- **The coupled projectors.** $P_{\mathrm{sym}}=\tfrac14(3e_0\otimes e_0-\sum_k e_k\otimes e_k)$ of trace $3$ and $P_{\mathrm{asym}}=\tfrac14(e_0\otimes e_0+\sum_k e_k\otimes e_k)$ of trace $1$, Hermitian, orthogonal, complete; they are the $\pm1$ spectral projectors of $F$ and the spectral projectors of $\tilde S^2$, with $\tilde S^2=2\hbar^2P_{\mathrm{sym}}$.
- **The four coupled idempotents.** $E_{1,\pm1}=P_\pm\otimes P_\pm$, $E_{1,0}=P_{\mathrm{sym}}-E_{1,1}-E_{1,-1}$, $E_{0,0}=P_{\mathrm{asym}}$; they are minimal Hermitian idempotents of trace one resolving the identity, and the total spin acts on them by $\tilde S_3E_{j,m}=m\hbar E_{j,m}$, $\tilde S^2E_{j,m}=j(j+1)\hbar^2E_{j,m}$, $\tilde S_\pm E_{j,m}=\hbar\sqrt{(j\mp m)(j\pm m+1)}\,|j,m\pm1\rangle\langle j,m|$.
- **Exchange symmetry.** $F E_{j,m}=(-1)^{1-j}E_{j,m}$: the singlet is antisymmetric, the triplet symmetric; the singlet is annihilated by the total ladder operators and is a zero divisor of the two-qubit algebra.
- **The Heisenberg coupling.** For $\tilde H=-J\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}$, the eigenvalues are $-J\hbar^2/4$ on the triplet and $+3J\hbar^2/4$ on the singlet, with splitting $J\hbar^2$; the Hamiltonian is the algebra element $\tilde H=-\tfrac{J\hbar^2}{2}F+\tfrac{J\hbar^2}{4}e_0\otimes e_0$.
- **Reduced states.** $\mathrm{Tr}_2(E_{1,\pm1})=P_\pm$ are pure; $\mathrm{Tr}_2(E_{1,0})=\mathrm{Tr}_2(E_{0,0})=\tfrac12 e_0$ are maximally mixed. The middle triplet member and the singlet are indistinguishable by their reduced states.
- **Two idempotent bases.** The coupled basis and the Bell basis are two orthogonal families of minimal idempotents of the same algebra, sharing the singlet and related by a Hadamard rotation.

All of this is a statement about $\mathbb{B}\otimes\mathbb{B}$; it presupposes the tensor-product composition rule, which the framework assumes rather than derives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit algebra |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $\mathrm{Tr}_1,\mathrm{Tr}_2$ | Partial traces |
| $\tilde S_k=\tfrac{\hbar}{2}ie_k$ | One-particle spin operators |
| $\tilde S_k^{(1)}=\tilde S_k\otimes e_0,\ \tilde S_k^{(2)}=e_0\otimes\tilde S_k$ | Factor spin operators |
| $\tilde S_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ | Total spin |
| $\tilde S_\pm=\tilde S_1\pm i\tilde S_2$ | Total ladder operators |
| $P_\pm(\hat z)=\tfrac12(e_0\pm ie_3)$ | One-particle idempotents |
| $F=\tfrac12(e_0\otimes e_0-\sum_k e_k\otimes e_k)$ | Exchange operator |
| $P_{\mathrm{sym}},P_{\mathrm{asym}}$ | Triplet and singlet projectors |
| $E_{j,m}$ | Coupled idempotents, $j\in\{1,0\}$ |
| $\tilde H=-J\sum_k\tilde S_k^{(1)}\tilde S_k^{(2)}$ | Heisenberg coupling |
| $J$ | Exchange constant (ferromagnetic $J>0$) |
| $\Phi(e_0)=I_2,\ \Phi(e_k)=-i\sigma_k$ | Matrix isomorphism |

## Further Reading

- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the addition of two spin-$\tfrac12$ systems, the triplet and singlet states, and the exchange interaction.
- Albert Messiah, *Quantum Mechanics* (North-Holland, 1961), for the two-spin system, the singlet–triplet structure, and the spin-exchange operator.
- Claude Cohen-Tannoudji, Bernard Diu, and Franck Laloë, *Quantum Mechanics* (Wiley, 1977), for the two-spin problem, the coupled basis, and the exchange interaction in the two-electron atom.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix formalism, partial traces, and the reduced states of a composite system.
- Daniel C. Mattis, *The Theory of Magnetism Made Simple* (World Scientific, 2006), for the Heisenberg exchange Hamiltonian, its spectrum, and the ferromagnetic–antiferromagnetic dichotomy.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for the two-qubit algebra, the swap operator, and the standard idempotent bases of the two-qubit space.
- R. P. Feynman, R. B. Leighton, and M. Sands, *The Feynman Lectures on Physics*, Vol. III (Addison-Wesley, 1965), for the two-spin system, the exchange splitting, and the algebraic treatment of the singlet and triplet.
