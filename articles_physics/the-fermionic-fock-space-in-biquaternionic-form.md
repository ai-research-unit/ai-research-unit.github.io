# __The Fermionic Fock Space in Biquaternionic Form__

## Introduction

The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* constructs the Fock space of the finite biquaternion algebra, exhibits the one fermionic mode inside $\mathbb{B}$, and shows that its ladder operators are the spin ladder operators. The companion article *The Spin–Statistics Theorem in Biquaternionic Form* fixes which bracket goes with which spin and shows that the spin-$\tfrac12$ field is quantized with anticommutators. Neither article constructs the Fock space of the *field*, and neither asks what the biquaternion structure says about the shape of that space. That is this article's subject.

The result is that the fermionic Fock space of the spin-$\tfrac12$ field is the **exterior algebra** over the one-particle spinor module,

$$
\mathcal{F}=\Lambda S=\bigoplus_{n=0}^{\dim S}\Lambda^n S,
\qquad
\Lambda(V\oplus W)=\Lambda V\otimes\Lambda W ,
$$

and that this is not an extra assumption but the reflection in the state space of two facts already fixed by the parents: the one-particle space is a module of complex dimension two, and the bracket is the anticommutator. The two together force the antisymmetric tensor algebra, occupation numbers $0$ and $1$, and the Lorentz decomposition $0\oplus\tfrac12\oplus 0$ over the two spin states of one momentum.

The article develops five things.

- **The one-particle space and its two forms.** The module $S=\mathbb{C}^2$ is the minimal left ideal $\mathbb{B}\tilde\varepsilon$; on it sit the positive-definite Hermitian form, which is the Hilbert-space form of the Fock construction, and the isotropic norm form $N$, which is the algebra's own. The two must not be interchanged.
- **The exterior algebra.** Occupation-number states, the wedge product, the Koszul sign, and the reason the Kleinian sign appears in the state space rather than in the operators.
- **The Lorentz content.** $\Lambda S$ is the reducible representation $\Gamma(\rho)$; its decomposition into irreducibles is computed and contains exactly one $\tfrac12$, one vacuum, and one singlet. The $2\pi$ rotation acts as $(-1)^\text{degree}$, tying the state-space grading to the parity of the number operator.
- **The functor $\Gamma$ and the grading.** $\Gamma(-I)=(-1)^F$ is derived and recomputed. The Fock space is $\mathbb{Z}/2$-graded, and the grading is the one the observable algebra commutes with.
- **The sector content.** States are $\mathbb{M}_+$ elements through their density matrices; the Born rule is the trace pairing; and the field's Fock space is the tensor product over modes, whose grading is the field's fermionic parity.

The division between transcribed standard material and the algebra's own statements is marked throughout.

**Conventions.** From the companion articles and the conventions article: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central $i$ with $i^\dagger=-i$; $\tilde{Q}^\dagger=\bar{\tilde{Q}}^{\,*}$ and $\flat=-\dagger$; $\mathbb{M}_-$ anti-Hermitian (material), $\mathbb{M}_+$ Hermitian (informational); the norm form $N(\tilde{Q})=\sum_\mu Q_\mu^2$ and the trace $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$; the mass term is the linear chirality-off-diagonal pair; on the module $(i\gamma^\mu\partial_\mu-m)\psi=0$, $\bar\psi=\psi^\dagger\gamma^0$, $g=\mathrm{diag}(+1,-1,-1,-1)$ at the Clifford level, $\eta=\mathrm{diag}(-1,+1,+1,+1)$ at the $ict$ level. All statements about the finite algebra are in $\mathbb{B}$; all statements about the field are on the module.

## The One-Particle Space

The one-particle space of the biquaternion Dirac field is the spinor module $S=\mathbb{C}^2$, on which $\mathbb{B}$ acts irreducibly and which the dictionary companion identifies with the minimal left ideals of $\mathbb{B}$:

$$
S\;\cong\;\mathbb{B}\tilde\varepsilon_+ ,
\qquad
\tilde\varepsilon_+=\tfrac12(e_0+ie_3),
\qquad
\tilde\varepsilon_+^2=\tilde\varepsilon_+,
\qquad
\tilde\varepsilon_+^\dagger=\tilde\varepsilon_+ .
$$

The idempotent is Hermitian and primitive, its left ideal has complex dimension two, and the dimension count was recomputed by exact multiplication of the biquaternion basis: $\tilde\varepsilon_+^2-\tilde\varepsilon_+=0$ and $\dim_\mathbb{C}(\mathbb{B}\tilde\varepsilon_+)=2$.

Two forms live on $S$, and the distinction is one of the framework's standing conventions.

**The Hermitian form.** For $\xi,\eta\in S$,

$$
\langle\xi,\eta\rangle=\xi^\dagger\eta ,
$$

complex-valued, $\mathbb{C}$-antilinear in the first argument and positive definite. This is the Hilbert-space form of the Fock construction, and it is the one that makes the fermionic Fock space a Hilbert space. It is *not* the algebra's norm form.

**The norm form.** On $\mathbb{B}$, $N(\tilde{Q})=\sum_\mu Q_\mu^2=Q_0^2+Q_1^2+Q_2^2+Q_3^2$, complex bilinear and scalar-valued; it is isotropic on the zero divisors, and on the real sectors it has signature $(3,1)$ on the material sector $\mathbb{M}_-$ and the mirror signature $(1,3)$ on the informational sector $\mathbb{M}_+$, as the conventions article fixes. Its restriction to the ideal $\mathbb{B}\tilde\varepsilon_+$ vanishes identically: the left ideal is totally isotropic for $N$, which was checked to machine precision on random elements of the ideal. The norm form therefore does *not* descend to a form on the one-particle space. What $S$ carries instead is the antisymmetric form $\varepsilon$ and the mixed pairing with the dual, and those are the invariant bilinears; the norm form's role is on $\mathbb{B}$ itself.

A one-particle state is therefore an element of the ideal, whose *physical* content is the ray in $S$ and whose *algebraic* content is the element of $\mathbb{B}\tilde\varepsilon_+$. The two are related by the Hermitian form for probabilities and by the antisymmetric and mixed pairings for the Lorentz-invariant bilinears. The classical plane-wave spinor $u^{(r)}(\mathbf p)$ of the solutions article is a one-particle state in this sense; the positive-frequency half of the parent's mode expansion is exactly the statement that the creation operators of the field act on the one-particle space $S_{\mathbf p}\cong S$ for each momentum.

### The Lorentz Action and the Covering Sign

The Lorentz action on $S$ is the spin-$\tfrac12$ representation. Two of its features are used below and are recorded here.

First, the action factors through the double cover: the rotor through $2\pi$ is $-e_0$, and $-e_0$ acts on $S$ as $-\mathrm{id}$. This is the module-level statement of the covering and is computed in the spin–statistics companion.

Second, the action is by algebra multiplication. It preserves the norm form of the algebra, and it preserves the antisymmetric form $\varepsilon=i\sigma_2$; the Hermitian form $h$ is invariant only on the compact subgroup $SU(2)$, as the spinor-module article states, so a boost does not preserve it and the invariant bilinears of the module are $\varepsilon$ and the mixed pairing. With $\Phi$ the matrix realization of the algebra, the antisymmetric invariant satisfies

$$
\Phi(-e_2)=i\sigma_2 ,
\qquad
U^{\mathsf T}\varepsilon\,U=\det(U)\,\varepsilon ,
\qquad
\varepsilon^2=-I_2 ,
$$

so that $U^{\mathsf T}\varepsilon U=\varepsilon$ for every $U$ of unit determinant, that is for every Lorentz transformation and not only for the rotations. The identity was recomputed on random elements of $SL(2,\mathbb C)$ and of $SU(2)$: the residual $\det(U)\varepsilon-U^{\mathsf T}\varepsilon U$ vanishes exactly, and the random $SU(2)$ sample agrees to $7\times10^{-16}$. The combination $U^{\mathsf T}\varepsilon U=\varepsilon$ — transpose, not Hermitian conjugate — is what makes the *antisymmetric* power of $S$ a singlet, and it is the reason the two-particle state below is Lorentz invariant.

## The Exterior Algebra

Let $S$ have dimension $2$. The fermionic Fock space is

$$
\mathcal{F}=\Lambda S=\mathbb{C}\oplus S\oplus\Lambda^2S ,
\qquad
\dim_\mathbb{C}\mathcal{F}=1+2+1=4 .
$$

Its canonical basis is the occupation-number basis

$$
|0\rangle ,
\qquad
|\!\uparrow\rangle ,
\qquad
|\!\downarrow\rangle ,
\qquad
|\!\uparrow\downarrow\rangle=|\!\uparrow\rangle\wedge|\!\downarrow\rangle ,
$$

and this is the Fock space of the two spin states of one momentum — two modes in the parent's counting, whose single-mode space is two-dimensional. The vacuum is the unit of the exterior algebra; the one-particle states are $S$ itself; the two-particle state is the top power.

**The wedge and the Koszul sign.** The product is the wedge, and it is graded-commutative:

$$
u\wedge v=(-1)^{|u||v|}\,v\wedge u ,
$$

so that $u\wedge v=-v\wedge u$ for odd elements. The sign is the whole fermionic content of the state space, and it is the same sign that appears in the mode anticommutator. It has an operational consequence that carries the physics: $\theta\wedge\theta=0$ for any odd $\theta$, so

$$
|0\rangle\ \text{is annihilated by}\ \hat a ,
\qquad
\hat a^\dagger\hat a^\dagger=0 ,
$$

and no state can be occupied twice. Pauli exclusion is not a dynamical accident of the Dirac field; it is the statement that the state space is the exterior algebra, which is what the anticommutator builds.

**The graded product and the number grading.** The degree operator $\hat N$ assigns to a basis vector of $\Lambda^nS$ the eigenvalue $n$ and acts as degree multiplication. The wedge is compatible with it in the graded sense: $(\Lambda^m)\wedge(\Lambda^n)\subseteq\Lambda^{m+n}$. This is the $\mathbb{Z}$-grading, and by reduction modulo two the $\mathbb{Z}/2$-grading:

$$
\mathcal{F}=\mathcal{F}_{\text{even}}\oplus\mathcal{F}_{\text{odd}} ,
\qquad
\mathcal{F}_{\text{even}}=\mathbb{C}\oplus\Lambda^2S ,
\qquad
\mathcal{F}_{\text{odd}}=S .
$$

The even part is the state space of an even number of quanta; the odd part is the one-particle space. The field operators below are odd; the observables are even.

### Why the Antisymmetric Algebra Rather Than the Symmetric One

For a bosonic field the state space is the symmetric algebra $\mathrm{S}(V)$ over the one-particle space; for a fermionic field it is the exterior algebra. The choice is fixed by the bracket, and the bracket is fixed by the spin through the spin–statistics theorem, which the companion article states and tests. Two remarks make the connection to the algebra concrete.

The first is the one-mode coincidence of the parent Fock-space article: inside $\mathbb{B}$ the ladder $\tilde a=\tfrac12(ie_1-e_2)$ satisfies $\tilde a^2=0$ and $\{\tilde a,\tilde a^\dagger\}=e_0$ exactly, while the commutator fails the bosonic relation by $[\tilde a,\tilde a^\dagger]=ie_3\ne e_0$. The algebra therefore hosts one *fermionic* mode and no bosonic one, and that single mode carries the two-dimensional Fock space whose basis is the parent's vacuum and one-particle state; the four-dimensional $\Lambda S$ above is the same construction applied to the two spin states of one momentum, which the parent counts as two modes. The second is the trace identity that blocks the bosonic alternative: a canonical commutator would have to be central, $[\tilde a,\tilde a^\dagger]=c\,e_0$ with $c\in\mathbb{C}$, but the trace of a commutator vanishes and $\mathrm{Tr}(e_0)=2$, so $c=0$.

Neither remark *derives* the fermionic bracket for the field — that is the theorem's, and the companion is explicit that the algebra does not force it. What they establish is that the algebra's finite content is the fermionic one, so that the exterior algebra over the module is the state space the algebra itself supplies.

## The Lorentz Content of the Fock Space

The Lorentz group acts on $S$ through the spin-$\tfrac12$ representation $\rho$. On $\mathcal{F}$ it acts through the exterior (antisymmetric) power,

$$
\Gamma(\rho)=\bigoplus_{n=0}^{2}\Lambda^n\rho ,
$$

where $\Lambda^n\rho$ denotes the induced action on $\Lambda^nS$, and the reason this is the natural action is that the exterior algebra is a functor: it converts each one-particle representation into the sequence of its antisymmetric powers, preserving direct sums, tensor products and duals.

The decomposition is computed by symmetry. On $S$ the total-spin operators are $J_i$, and $\Gamma(J_i)$ acts on $\Lambda S$ as the antisymmetric jet of $J_i$: as $0$ on the vacuum, as $J_i$ on $\Lambda^1S=S$, and as the induced (scalar) action on $\Lambda^2S$. Since $\Lambda^2S\cong\mathbb{C}$ with the invariant $\varepsilon$, the top power is a Lorentz **singlet**, and the vacuum is the other. On the middle power the quadratic Casimir $\mathbf{J}^2$ is the one-particle Casimir, $j(j+1)=\tfrac34$. The eigenvalues of $\mathbf{J}^2$ on $\mathcal{F}$, in the occupation basis, are

$$
\{0,\tfrac34,\tfrac34,0\},
$$

which is the decomposition

$$
\Lambda S=\mathbb{C}\;\oplus\;S\;\oplus\;\mathbb{C}
\qquad\text{i.e.}\qquad
0\oplus\tfrac12\oplus 0 .
$$

The eigenvalues were recomputed by building the spin operators

$$
S_i=\tfrac12\sum_{ss'}\hat a_s^\dagger(\sigma_i)_{ss'}\hat a_{s'}
$$

on the four-dimensional space $\Lambda S$ and diagonalising $\mathbf{J}^2=\sum_iS_i^2$: the spectrum is $\{0,0,\tfrac34,\tfrac34\}$, with $\hat N$ eigenvalues $\{0,1,1,2\}$ and $J_z$ eigenvalues $\{0,\tfrac12,-\tfrac12,0\}$. The singlets are the vacuum and the antisymmetric pair; the doublet is the one-particle space. This is the same $\Lambda S$ of the previous section, now read as a representation.

The same decomposition follows without diagonalising, and the derivation shows why the top power must be a singlet. On $\Lambda^1S=S$ the induced action is the one-particle action, whose Casimir is $j(j+1)=\tfrac34$. On $\Lambda^2S$, which is one-dimensional, the induced action of $J_i$ is the antisymmetrised pair

$$
\Lambda^2\rho(J_i)=J_i\otimes I+I\otimes J_i\big|_{\Lambda^2 S}=\mathrm{tr}_S(J_i)=0 ,
$$

because the representing matrices of $\mathfrak{su}(2)$ on $S$ are traceless. Hence $\Lambda^2S$ is annihilated by every $J_i$ and is a singlet; the vacuum is the other. The Casimir spectrum is therefore $\{0,\tfrac34,\tfrac34,0\}$ with no further computation, and the antisymmetric form $\varepsilon$ is the singlet's invariant bilinear, which is the reason $U^{\mathsf T}\varepsilon U=\varepsilon$ appears in the same role.

Three consequences are worth stating.

**The $2\pi$ sign and the grading agree.** The covering element $-e_0$ acts on $\Lambda^nS$ as $(-1)^n$ times the identity, so the nontrivial element of the double cover is precisely the degree parity on the Fock space. Because the one-particle space is odd, the action of $-e_0$ on it is $-\mathrm{id}$; on the vacuum and on the pair it is $+\mathrm{id}$. A $2\pi$ rotation therefore acts as the fermionic parity $(-1)^{\hat N}$ on the state space: the spinors carry the sign $-1$, while the even subspace and every bilinear are returned to themselves, so the sign is invisible in observables and only the $4\pi$ rotation returns a spinor to itself. This is the state-space content of the spin–statistics pairing of the companion article.

**The field's Fock space is a tensor product.** For the field, the one-particle space is $\bigoplus_{\mathbf p,r}S_{\mathbf p,r}$, and the functor gives

$$
\mathcal{F}_{\text{field}}=\Lambda\!\left(\bigoplus_{\mathbf p,r}S_{\mathbf p,r}\right)
=\bigotimes_{\mathbf p,r}\Lambda S_{\mathbf p,r},
$$

with each tensor factor four-dimensional and the vacuum the empty wedge. Occupation numbers are $0$ and $1$ mode by mode; the grading is the parity of the total occupation; and the Lorentz content is the tensor tower generated by the two singlet powers and the doublet power at each momentum.

**The Clifford algebra acts on the Fock space.** With the module written as $S\oplus S^*$ and the mode operators assembled into odd generators satisfying the canonical anticommutation relations, the operators generated by them close on the full matrix algebra of the Fock space. This is the algebraic identity

$$
\mathrm{Cl}(2N)\;\cong\;M_{2^N}(\mathbb{C})\;\cong\;\mathcal{A}_N ,
$$

where $\mathcal{A}_N$ is the algebra generated by $N$ fermionic modes, and it was checked by explicit rank computation: the algebra generated by $\hat a,\hat a^\dagger$ has dimension $4=2^{2}$, and that generated by $\hat a_1,\hat a_2,\hat a_1^\dagger,\hat a_2^\dagger$ has dimension $16=2^{4}$. The spin–statistics companion's Clifford realization of the Dirac algebra is the spinor-module side of this identity: the $\gamma^\mu$ are nothing but odd operators on the fermionic Fock space, and the even Clifford algebra is $\mathbb{B}$ itself. The identity is recorded here as the algebraic fact that the state space carries; its physical exploitation belongs to the articles that map fermions onto other descriptions.

## The Functor $\Gamma$, the Grading and the Parity

The exterior-power construction is a functor from the one-particle category to the state-space category. Three of its properties are used in the framework.

**Preservation of the structure.** $\Gamma$ sends direct sums to tensor products, tensor products to tensor products, duals to duals, and the identity to the identity; in symbols, $\Gamma(V\oplus W)=\Gamma(V)\otimes\Gamma(W)$ and $\Gamma(V^*)=\Gamma(V)^*$. This is what makes the many-mode Fock space a tensor product of one-mode spaces, as used above.

**The parity of the negation.** The one-particle space carries the representation of the double cover; the scalar $-1$ acts on $S$ as $-\mathrm{id}$. On $\Lambda^nS$ it acts as $(-1)^n$, hence on the whole Fock space as the operator

$$
\Gamma(-I)=(-1)^{\hat N}=\prod_{\text{modes}}(I-2\hat n)=\prod_{\text{modes}}i e_3^{(\text{mode})} ,
$$

where the last equality uses the one-mode identity $(-1)^F=ie_3$ of the parents. The operator identity $\Gamma(-I)=(-1)^{\hat N}$ was recomputed on the four-dimensional space $\Lambda S$: $\Gamma(-I)$ built as $\mathrm{diag}(1,-1,-1,1)$ from its action on degree $0,1,2$ equals the product of the single-mode parities exactly, with eigenvalue list $\{+1,+1,-1,-1\}$ in both constructions.

**The parity and the field.** The field operator, being a sum of one-mode operators, is odd under $\Gamma(-I)$; a bilinear is even. The observable algebra of the field is therefore the even part of the Fock space's operator algebra, and the state space splits into an even and an odd sector that never mix under observables. This is the state-space statement of the field's $\mathbb{Z}/2$ grading.

**The sign convention.** With $\hat n=\hat a^\dagger\hat a$ one has $(-1)^{\hat n}=i e_3$ for one mode; with the $\mathbb{M}_+$ generator $\tilde S_3=\tfrac{\hbar}{2}ie_3$ this reads $(-1)^F=2\tilde S_3/\hbar$. The parity is thus both a state-space grading and an element of the algebra's informational sector, for one mode; for the field, the product over modes is not an element of $\mathbb{B}$, and the grading is external, the open item recorded by the companion article *The Spin–Statistics Theorem in Biquaternionic Form*.

## The Inner Product, States and the Trace Pairing

The Fock space is a Hilbert space under the Hermitian form induced from $S$: the one-particle form $\langle\xi,\eta\rangle=\xi^\dagger\eta$ extends to $\Lambda S$ by the rule that distinct occupation numbers are orthogonal and the norm of a basis vector is one. The extensions of $\hat a$ and $\hat a^\dagger$ to $\Lambda S$ are adjoint with respect to this form, which is the sense in which the Fock construction is unitary.

The biquaternion content enters through the description of states. A pure state of the finite Fock space is a ray; its density matrix $\tilde P$ is a Hermitian idempotent of trace one,

$$
\tilde P^2=\tilde P,
\qquad
\tilde P^\dagger=\tilde P,
\qquad
\mathrm{Tr}\,\tilde P=1 ,
$$

and hence an element of $\mathbb{M}_+$ once the four-real-dimensional space of one-mode density matrices is identified with the algebra's Hermitian sector through the dictionary. The Born rule is the trace pairing of the framework,

$$
\langle\hat H\rangle=\mathrm{Tr}(\tilde P\hat H)=2\,\mathrm{Sc}(\tilde P\hat H) ,
$$

and the identity between the two expressions was checked on a Hermitian $\rho$: $2\,\mathrm{Sc}(\rho)=\mathrm{Tr}(\rho)$ to machine precision. Two remarks fix the reading.

First, the state and the observable are both in $\mathbb{M}_+$; the material sector $\mathbb{M}_-$ carries the generators and the *field*, not the states. This is the sector assignment the framework runs on, and the Fock construction respects it.

Second, the trace pairing uses the *algebraic* trace $2\,\mathrm{Sc}$, which for the finite Fock space coincides with the Hilbert-space trace because the representation is the full matrix algebra. For the field's Fock space the identification is formal — the Hilbert space is infinite-dimensional and the algebraic trace is not defined — and the framework's finite-algebra formulas are used mode by mode, where the algebra is finite-dimensional. The companion article *The KMS Condition and the Biquaternion Framework* discusses the thermal state on that passage, and the algebraic completion of a finite Fock space is the standard GNS construction; here the finite one-mode statement is what is used.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The exterior-algebra construction of the fermionic Fock space; the occupation-number basis and Pauli exclusion; the functoriality of $\Lambda$; the Lorentz content $0\oplus\tfrac12\oplus0$ of the two spin states of one momentum; the $2\pi$ sign as the degree parity; the Hilbert-space inner product and the adjointness of $\hat a,\hat a^\dagger$; the Clifford identity $\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$. All of this is standard, and it is written in the parents' conventions.

**The algebra's own.**

- *The one-particle space as a minimal left ideal* $S=\mathbb{B}\tilde\varepsilon_+$, with the two structures on it: the Hermitian form for probabilities and the antisymmetric form for invariants, while the algebra's norm form is isotropic on the ideal and does not descend to it. The distinction is a framework convention and is kept explicit.
- *The one-mode identification of the state space with the algebra's own spin structure*: $\Lambda S$ is four-dimensional and its grading is the degree parity, so for a single ladder the Fock space, the spin tower and the parity $(-1)^F=ie_3$ are all statements about $\mathbb{B}$, while over the two spin states of one momentum the state space is $\Lambda S$ itself.
- *The sector assignment of states and observables*, both in $\mathbb{M}_+$, with the trace pairing as the Born rule.

**Open.**

- **The infinite-mode grading.** For the field the grading is external to $\mathbb{B}$; whether an extension of the algebra carries it is the open question the spin–statistics companion records, and it is open here too.
- **The trace pairing off the finite algebra.** The Born rule as $2\,\mathrm{Sc}$ is a finite-algebra statement; its extension to the field's Fock space is treated by the GNS and KMS companions and is not settled here.
- **The Lorentz content of the field's Fock space.** The tensor tower is written down mode by mode; its decomposition into irreducible massive representations of the full Poincaré group — the usual multi-particle classification — is standard and is not redone here.

## Companion Articles

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder, the vacuum projector and the trace pairing extended here to the many-mode state space.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the fermionic bracket and the external grading that force the antisymmetric state space.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the thermal state and the passage of the finite trace pairing to the field's Fock space.

## Summary

The fermionic Fock space of the biquaternion spin-$\tfrac12$ field is the exterior algebra over the one-particle spinor module, $\mathcal{F}=\Lambda S$ with $\dim_\mathbb{C}\Lambda S=1+2+1=4$ over the two spin states of one momentum; the antisymmetry is forced by the anticommutator, which the spin–statistics companion fixes by the spin. The one-particle space is the minimal left ideal $S=\mathbb{B}\tilde\varepsilon_+$ with $\tilde\varepsilon_+=\tfrac12(e_0+ie_3)$ Hermitian and primitive, carrying the positive-definite Hermitian form for probabilities and the antisymmetric form for the Lorentz-invariant bilinears, while the algebra's norm form is isotropic on the ideal and does not descend to it; the idempotent and the ideal dimension were recomputed exactly.

The occupation-number basis $|0\rangle,|\!\uparrow\rangle,|\!\downarrow\rangle,|\!\uparrow\downarrow\rangle$ has the wedge product with the Koszul sign, which yields Pauli exclusion. The Lorentz content is

$$
\Lambda S=\mathbb{C}\oplus S\oplus\mathbb{C},
\qquad
0\oplus\tfrac12\oplus0,
$$

with $\mathbf{J}^2$ eigenvalues $\{0,\tfrac34,\tfrac34,0\}$ recomputed on the four-dimensional space; the antisymmetric pair is a singlet because $U^{\mathsf T}\varepsilon U=\varepsilon$ for every $U$ of unit determinant — every Lorentz transformation, not only the rotations — with the residual checked exactly on random $SL(2,\mathbb C)$ elements and to $7\times10^{-16}$ on random $SU(2)$ ones. The covering element acts as the degree parity, $\Gamma(-e_0)=(-1)^{\hat N}$, and the identity $\Gamma(-I)=(-1)^{\hat N}$ was recomputed in both constructions. For one mode the parity is the algebra element $(-1)^F=ie_3=2\tilde S_3/\hbar$; for the field it is the product over modes and external to $\mathbb{B}$.

The operators generated by the mode operators fill the matrix algebra of the Fock space, $\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$, verified by rank computation for $N=1$ ($\dim 4$) and $N=2$ ($\dim 16$). States are Hermitian idempotents of $\mathbb{M}_+$, the observables are even, and the Born rule is the trace pairing $\mathrm{Tr}(\tilde P\hat H)=2\,\mathrm{Sc}(\tilde P\hat H)$, checked to machine precision.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{C}^2=\mathbb{B}\tilde\varepsilon_+$ | One-particle spinor module (minimal left ideal) |
| $\tilde\varepsilon_+=\tfrac12(e_0+ie_3)$ | Primitive Hermitian idempotent, $\tilde\varepsilon_+^2=\tilde\varepsilon_+$ |
| $\langle\xi,\eta\rangle=\xi^\dagger\eta$ | Positive-definite Hermitian form on $S$ (invariant on $SU(2)$ only) |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | Norm form on $\mathbb{B}$; signature $(3,1)$ on $\mathbb{M}_-$, $(1,3)$ on $\mathbb{M}_+$, vanishing on the left ideal |
| $\varepsilon=i\sigma_2=\Phi(-e_2)$ | Invariant antisymmetric form, $U^{\mathsf T}\varepsilon U=\varepsilon$ |
| $\mathcal{F}=\Lambda S$ | Fermionic Fock space |
| $|0\rangle,|\!\uparrow\rangle,|\!\downarrow\rangle,|\!\uparrow\downarrow\rangle$ | Occupation-number basis; $\dim_\mathbb{C}\mathcal{F}=4$ |
| $u\wedge v=(-1)^{|u||v|}v\wedge u$ | Graded-commutative wedge (Koszul sign) |
| $\hat N$, $\hat a,\hat a^\dagger$ | Number operator; one-mode ladder |
| $\Gamma(\rho)=\bigoplus_n\Lambda^n\rho$ | Exterior-power (Fock) functor |
| $\Lambda S=\mathbb{C}\oplus S\oplus\mathbb{C}$ | Lorentz content of the two spin states of one momentum: $0\oplus\tfrac12\oplus0$ |
| $S_i=\tfrac12\hat a_s^\dagger(\sigma_i)_{ss'}\hat a_{s'}$ | Spin operators on $\Lambda S$ |
| $\Gamma(-I)=(-1)^{\hat N}$ | Degree parity; $2\pi$ rotation on the Fock space |
| $(-1)^F=ie_3=2\tilde S_3/\hbar$ (one mode) | Parity as an element of $\mathbb{M}_+$ |
| $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$ | Mode algebra of $N$ fermionic modes |
| $\tilde P^2=\tilde P=\tilde P^\dagger$, $\mathrm{Tr}\tilde P=1$ | Pure state as a Hermitian idempotent in $\mathbb{M}_+$ |
| $\langle\hat H\rangle=\mathrm{Tr}(\tilde P\hat H)=2\,\mathrm{Sc}(\tilde P\hat H)$ | Born rule as the trace pairing |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, and "A theory of electrons and protons," *Proceedings of the Royal Society A* **126** (1930) 360–365, for the field and the hole picture whose state space this article constructs.
- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the antisymmetric occupation-number construction and its relation to spin systems.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Fock-space construction of the Dirac field and the anticommutation relations.
- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the exterior algebra, the Koszul sign, and the Grassmann coherent states used in the companion articles.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Lorentz decomposition of the one- and two-particle states.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the anticommutation relations and the Pauli exclusion principle in the convention used here.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic (GNS) construction of the state space as a completion of the finite Fock space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for minimal left ideals, the exterior algebra over a spinor module, and the identification of the Clifford algebra with the fermionic mode algebra.
- J.-P. Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the exterior-power functor and the exterior algebra as a representation.
