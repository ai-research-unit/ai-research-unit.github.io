# __Kramers Degeneracy and Antiunitary Symmetry in Biquaternionic Form__

## Introduction

A symmetry that reverses time is not represented by a unitary operator on the state space; it is represented by an **antiunitary** one, and that one word carries the whole of Kramers' theorem. The companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* establishes that the biquaternion algebra carries three antilinear involutions — complex conjugation $^*$, Hermitian conjugation $^\dagger$, and the anti-Hermitian conjugation $\flat=-\dagger$ — alongside the *linear* quaternion conjugation, that their fixed spaces are four distinct subspaces, and that the algebra's real structure $\flat$ and the module's charge conjugation $\mathcal{C}$ are **different real structures on different spaces**. The companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form* and the spin–statistics companion fix the $2\pi$ covering sign. This article puts those two ingredients together.

It establishes four things.

- **Antiunitarity is intrinsic; the physical $\mathcal T$ is constructed.** The algebra supplies the antilinear involution and the rotation elements, but the time-reversal operator of the spinor module is a *module-level* antilinear map, built as a rotation composed with the conjugation — the same algebra-versus-module discipline that the mass article enforces for the mass.
- **The sign of $\mathcal T^2$ is the $2\pi$ rotor.** On the spinor module the rotation element of the construction is real and squares to $-e_0$. Consequently
  $$\mathcal T^2=U U^*=U^2=-e_0 ,$$
  the same element that the spin–statistics companion identifies as the rotation through $2\pi$. Kramers degeneracy is the $2\pi$ sign seen on the state space.
- **Kramers degeneracy.** For every $\mathcal T$-invariant Hamiltonian with $\mathcal T^2=-1$, the spectrum is even-degenerate, with a proof that uses only antiunitarity. The proof, the orthogonality of the partner, and the degeneracy itself were recomputed.
- **The quaternionic structure.** The algebra's imaginary units supply the antiunitary $J$ with $J^2=-e_0$ that makes the state space a vector space over the quaternions; the commutant of $\mathcal T$ was computed and is two-complex-dimensional, which is the quaternionic line. Kramers degeneracy is the statement that the state space's unit is not $\mathbb{C}$ but $\mathbb{H}$.

The article closes with what breaks the symmetry, and with the framework's standing disclaimer: the algebra names the axis along which the symmetry is lost, and does not choose it.

**Conventions.** From the companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, $e_0=1$, $e_k^2=-e_0$, $e_1e_2=e_3$ and cyclic, central $i$ with $i^\dagger=-i$; the antilinear involutions $\tilde{Q}^*$ (complex conjugation), $\tilde{Q}^\dagger=\bar{\tilde{Q}}^{\,*}$ (Hermitian), $\tilde{Q}^\flat=-\tilde{Q}^\dagger$ (anti-Hermitian), and the linear quaternion conjugation $\bar{\tilde{Q}}$; $\flat(\tilde\Psi)=+\tilde\Psi$ on $\mathbb{M}_-$ and $-\tilde\Psi$ on $\mathbb{M}_+$; $\mathbb{M}_-=i\,\mathbb{M}_+$; $\mathrm{Tr}=2\,\mathrm{Sc}$; the module carries $(i\gamma^\mu\partial_\mu-m)\psi=0$, $\bar\psi=\psi^\dagger\gamma^0$; the spin generators are $\tilde S_k=\tfrac{\hbar}{2}ie_k$ with $[\tilde S_a,\tilde S_b]=i\hbar\epsilon_{abc}\tilde S_c$, and the rotation by angle $\theta$ about the unit direction $n$ in the module is $R(\theta)=\exp(\tfrac{\theta}{2}\,n\cdot e)$ with $R(2\pi)=-e_0$; the dictionary representative is $\Phi(e_k)=-i\sigma_k$, $\Phi(ie_k)=\sigma_k$.

## Antiunitary Maps and the Two Spaces

**Antiunitary.** A map $\mathcal T$ on a complex Hilbert space is antiunitary when it is antilinear and preserves the transition probabilities,

$$
\mathcal T(\alpha u+\beta v)=\alpha^*\,\mathcal T u+\beta^*\,\mathcal T v ,
\qquad
\langle\mathcal T u,\mathcal T v\rangle=\overline{\langle u,v\rangle} ,
$$

so that $|\langle\mathcal T u,\mathcal T v\rangle|=|\langle u,v\rangle|$ and the map is a symmetry of the ray space. Every antiunitary map is of the form $\mathcal T=UK$ with $U$ unitary and $K$ a fixed antilinear involution; the pair $(U,K)$ is not unique, but the *sign* of $\mathcal T^2$ is a property of $\mathcal T$ alone.

**The algebra's antilinear structure.** The companion article tabulates three antilinear involutions, $\dagger$, $\flat$ and $^*$, with fixed spaces of real dimensions $4$, $4$ and $4$ — the two-real-dimensional fixed space belongs to quaternion conjugation, which is linear; the two sectors are the fixed spaces of $\flat$ ($\mathbb{M}_-$) and $\dagger$ ($\mathbb{M}_+$), and $\flat$ acts on them as $+$ and $-$. Antilinearity is therefore not an add-on to the framework; it is present three times over, and the sectors are among its fixed spaces.

**The discipline.** Antiunitarity on the algebra and antiunitarity on the module are different statements, exactly as the mass article insists for the two real structures. A map like $\flat$ is an involution of $\mathbb{B}$; a time-reversal operator is a map of the module. The construction below uses both and does not identify them: the *algebra* supplies the rotation element $U$ and the conjugation the module carries, and the *product* is the module's $\mathcal T$. The one place where the algebra becomes indispensable is the sign, because $U^2$ is an element of $\mathbb{B}$ and its value can be read off there.

## Time Reversal on the Spinor Module

**The construction.** On the spin-$\tfrac12$ module the rotation element for an angle $\pi$ about the unit direction $n$ is

$$
U=\exp\!\Big(\frac{\pi}{2}\,n\cdot e\Big)=\cos\frac{\pi}{2}+(n\cdot e)\sin\frac{\pi}{2}=n\cdot e ,
\qquad
(n\cdot e)^2=-e_0 ,
$$

using $(n\cdot e)^2=n^2e_0^2=-e_0$ for a unit real direction. Two properties matter:

$$
U^*=U ,
\qquad
U^2=-e_0 .
$$

The first says the rotation element of the spinor module is **real** under the algebra's complex conjugation — it is built from the quaternion units, which complex conjugation fixes, and not from the central $i$, which it reverses. The second says it squares to minus the identity, because the imaginary quaternion units do.

**The sign.** With the module's conjugation $K$ — the antilinear involution that realizes the algebra's $^*$ on the module and turns $\dagger$ into the Hermitian adjoint — define

$$
\mathcal T=U\,K .
$$

Then $K^2=\mathrm{id}$ and $KUK=U^*$ for every $U$, so

$$
\boxed{\ \mathcal T^2=U\,K\,U\,K=U\,U^*=U^2=-e_0\ }
$$

for every choice of axis $n$: the sign does not depend on the axis, only on the dimension of the representation. This is the framework's derivation of $\mathcal T^2=-1$ for the spin-$\tfrac12$ module, and it uses nothing but the reality of the rotation element and the imaginary quaternion units' square.

**Why this is the $2\pi$ sign.** The rotation by $2\pi$ about the same axis is

$$
R(2\pi)=\exp(\pi\,n\cdot e)=\cos\pi+(n\cdot e)\sin\pi=-e_0 ,
$$

the covering element that the spin–statistics companion identifies as the half-integer signature, and the same $-e_0$ that appears as the nontrivial element of the double cover. The equality

$$
\mathcal T^2=R(2\pi)
$$

is best read directly: since $U=\exp(\tfrac{\pi}{2}n\cdot e)$ and $R(2\pi)=\exp(\pi n\cdot e)$, the product $UU^*=U^2$ **is** $R(2\pi)$, and it equals $-e_0$ for the spinor. So

$$
\mathcal T^2=R(2\pi)=(-1)^{2s}\,e_0 ,
$$

which is the standard result: $-1$ for half-integer spin, $+1$ for integer spin. In the framework it is not an independent fact but the same covering sign that fixes the spin–statistics pairing. Kramers degeneracy and the fermionic $2\pi$ phase are one sign seen in two places.

**The standard realization.** On the two-component spinor the standard representative of $\mathcal T$ is $\mathcal T=i\sigma_y K$ with $K$ the componentwise conjugation; the representative of the rotation element is $i\sigma_y$, which is a real matrix, and $U^2=-I_2$. The verification below uses this representative and confirms all the algebra-level claims: $U$ real, $U^2=-I$, $\mathcal T$ antiunitary, $\mathcal T^2=-1$.

## Kramers Degeneracy

**The theorem.** Let $H$ be a bounded Hermitian operator on a complex Hilbert space on which an antiunitary $\mathcal T$ acts with $[\mathcal T,H]=0$ and $\mathcal T^2=-1$. Then every eigenvalue of $H$ has even multiplicity.

**The proof.** The proof needs two lines and no model.

*(i) The partner is degenerate.* If $Hv=Ev$ then $H(\mathcal Tv)=\mathcal T(\mathcal T^{-1}H\mathcal T)v$. Since $[\mathcal T,H]=0$ we have $\mathcal T H=H\mathcal T$, and applying $\mathcal T$ to $Hv=Ev$ gives $H(\mathcal Tv)=E^*(\mathcal Tv)=E(\mathcal Tv)$ because $E$ is real for a Hermitian $H$. So $\mathcal Tv$ is an eigenvector with the same eigenvalue.

*(ii) The partner is orthogonal, hence independent.* Using antiunitarity with $\mathcal T^2v=-v$,

$$
\langle \mathcal Tv,v\rangle=\langle \mathcal Tv,-\mathcal T^2v\rangle=-\langle \mathcal Tv,\mathcal T(\mathcal Tv)\rangle
=-\overline{\langle v,\mathcal Tv\rangle}=-\langle\mathcal Tv,v\rangle ,
$$

where the last step uses the Hermiticity of the inner product. Hence $\langle\mathcal Tv,v\rangle=0$. Since $\mathcal Tv$ is orthogonal to $v$ and non-zero ($\|\mathcal Tv\|=\|v\|$ by antiunitarity), it is an independent eigenvector with the same energy, and the multiplicity is even.

**The three ingredients, and which one is the framework's.** The argument used antiunitarity, $\mathcal T^2=-1$, and $[\mathcal T,H]=0$. The first is the definition of the symmetry class; the third is the assumption of symmetry; the second is the **sign**, and it is the only one that the biquaternion algebra supplies — as $UU^*=U^2=-e_0$ above. The framework therefore does not prove Kramers' theorem, and does not need to: it explains why the sign in the hypothesis is minus.

**Physical content of the pairing.** The pair $\{v,\mathcal Tv\}$ is a **Kramers doublet**. Its consequences are standard and worth naming, because they are the theorem's empirical face: a system with an odd number of electrons has every level at least doubly degenerate in the absence of a magnetic field; the degeneracy is lifted only by a perturbation that is not $\mathcal T$-invariant, which is why a magnetic field splits a Kramers pair linearly; in a solid with strong spin–orbit coupling the same pairing underlies the helical protection of surface states; and the theorem holds for any half-integer total spin, because $\mathcal T^2=(-1)^{2s}$ is all that the proof ever uses.

**What the theorem does not say.** It says nothing about the *size* of the degeneracy beyond its parity, nothing about degeneracies that are not Kramers pairs, and nothing when the symmetry is approximate. It also requires that $\mathcal T$ be a symmetry of the Hamiltonian; an open system with gain and loss, or a Hamiltonian with a $\mathcal T$-odd term, is outside its hypotheses. The framework's statements are correspondingly narrow.

## Verification

The statements above are finite and were recomputed in the two-component and four-component realizations.

**Antiunitarity and the sign.** With $\mathcal T=i\sigma_yK$ on $\mathbb{C}^2$, the representative $U=i\sigma_y$ is real (maximum entry-wise imaginary part $0$) and satisfies $U^2=-I_2$. Applying $\mathcal T$ to the two basis vectors gives $\mathcal T^2e_b=-e_b$ for $b=1,2$, and the antiunitarity relation $\langle\mathcal Tu,\mathcal Tv\rangle=\overline{\langle u,v\rangle}$ holds to machine precision on random vectors, with maximum error $0$. The Kramers orthogonality $\langle\mathcal Tv,v\rangle=0$ holds for random $v$, with maximum modulus $0$ over five trials.

**A degenerate pair.** On $\mathbb{C}^4=\mathbb{C}^2\otimes\mathbb{C}^2$ with the antiunitary $\mathcal T=U\otimes I_2$ acting on the first factor and $H=I_2\otimes h$ with $h=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ on the second, one has $[\mathcal T,H]=0$ exactly ($\|THT^{-1}-H\|=0$). The vector $v=\tfrac1{\sqrt2}(e_1\otimes(1,1))$ satisfies $Hv=3v$ with residual $0$, its partner $\mathcal Tv=\tfrac{1}{\sqrt2}(e_2\otimes(1,1))$ — up to the sign carried by $\sigma_y$ — satisfies $H(\mathcal Tv)=3(\mathcal Tv)$ with residual $0$, and $\langle v,\mathcal Tv\rangle=0$ exactly. The doublet is the theorem's conclusion, exhibited.

**The opposite sign.** For $\mathcal T^2=+1$ no degeneracy is enforced. With a random real symmetric $H$ on $\mathbb{C}^4$ — which is invariant under conjugation, the $\mathcal T^2=+1$ case — the spectrum is $\{-3.01553,-1.70328,0.12807,2.44612\}$, four distinct levels with minimum gap $1.31225$. The contrast is the theorem: the degeneracy is a consequence of the sign, not of the symmetry alone.

**The antisymmetric form.** The pairing that makes each doublet one quaternionic line is the invariant antisymmetric form of the spinor, $\varepsilon=i\sigma_y$, and its invariance was recomputed: for five random $SU(2)$ elements $U=\exp(i\theta\,\mathbf n\cdot\boldsymbol\sigma/2)$, the identity

$$
U^{\mathsf T}\varepsilon\,U=\varepsilon
$$

held with maximum error $1.1\times10^{-16}$. The Kramers partner is the $\varepsilon$-contraction of the state, $\mathcal Tv=\varepsilon v^*$, so the antisymmetric form is what converts the antiunitary structure into a definite partner, and its invariance under the spin rotations is why the doublet is not split by a rotation-invariant perturbation.

**The quaternionic commutant.** The operators on $\mathbb{C}^2$ commuting with $\mathcal T$ (i.e. satisfying $UM^*U^{-1}=M$) form a real four-dimensional space, hence a two-complex-dimensional algebra — the quaternionic line $\mathbb{H}$. The dimension was computed by a rank count of the eight real linear conditions on the eight real parameters of $M$: rank $4$, solution dimension $4$ over $\mathbb{R}$ and $2$ over $\mathbb{C}$.

**The counting of $\mathcal T$-invariant Hamiltonians.** The degeneracy has a parameter count behind it. On $\mathbb{C}^{2N}$ with $\mathcal T^2=-1$, an invariant Hermitian operator can be written in the block form

$$
H=\begin{pmatrix}A & B\\ -B^* & A^*\end{pmatrix},
\qquad
A=A^\dagger ,
\qquad
B=-B^{T} ,
$$

which is Hermitian and satisfies $[\mathcal T,H]=0$ identically; the two conditions were verified on a random instance (residual $0$ in both). The real dimension count is then

$$
\dim_\mathbb{R}\{A\text{ Hermitian}\}+\dim_\mathbb{R}\{B\text{ complex antisymmetric}\}
=N^2+N(N-1)=N(2N-1),
$$

against $4N^2$ for a general Hermitian operator of the same size. The dimension was also obtained independently by a rank count of the invariance conditions, for $N=1,2,3$, giving $(1,6,15)=N(2N-1)$ in each case, with the constraint rank $N(2N+1)$. The antisymmetric block $B$ is the pairing structure on the Kramers pairs — the same antisymmetric form that the two-particle state of the spin-$\tfrac12$ Fock space carries — and its antisymmetry is why the pair behaves as a single quaternionic line rather than as two independent states.

## The Quaternionic Structure

The commutant computation is not an accident of the two-dimensional example; it is the structure that the algebra explains. On a complex Hilbert space, an antiunitary $J$ with $J^2=-1$ is a **quaternionic structure**: it lets one define $j\,v=Jv$ and, together with the complex $i$, generate the quaternion units acting on the space. The state space then has two units, not one, and its dimension as a quaternionic vector space is half its complex dimension.

The biquaternion algebra supplies such a $J$ intrinsically. Its imaginary units are precisely elements squaring to $-e_0$ — the same relation that $J$ satisfies — and the rotation element $U=n\cdot e$ of the construction is a *unit* imaginary element of the algebra. So the chain of identifications is

$$
U\ \text{(imaginary unit of }\mathbb{B}\text{)}
\;\longrightarrow\;
J=U K
\;\longrightarrow\;
J^2=U U^*=-e_0 ,
$$

and $J$ is the quaternionic structure. Two consequences follow.

- **Kramers degeneracy is the quaternionic dimension.** If the state space is quaternionic with a $\mathbb{C}$-dimension of $2N$, every $\mathbb{C}$-energy level is at least doubly degenerate, because a quaternionic line has complex dimension two. The theorem and the structure are the same statement.
- **The three imaginary units are the three axes of the symmetry.** $\mathbb{B}$ contains three independent imaginary elements $e_1,e_2,e_3$, whose representatives are the three Pauli directions; the choice of which one names the axis of the time-reversal rotation is the choice of a spin axis. The algebra supplies all three and distinguishes none.

**The relation to the mass article.** The mass article's lesson and this article's are the same lesson in two contexts: the algebra offers an antilinear structure, but a *physical* antilinear object on the module — a Majorana mass there, a time reversal here — must be constructed on the module, and the two real structures must not be substituted for one another. What the algebra does supply, in both cases, is the sign: there it is the sector sign of $\flat$, here it is the covering element $-e_0$.

## The Three Symmetry Classes

The value of $\mathcal T^2$ is not a detail of the operator; it selects the symmetry class, and the classification is standard.

| $\mathcal T^2$ | Class | Structure on the state space | Enforced degeneracy |
|---|---|---|---|
| no antiunitary symmetry | unitary | complex | none |
| $+e_0$ | orthogonal | real | none |
| $-e_0$ | symplectic | quaternionic | Kramers (even) |

The three rows are the three ways a complex Hilbert space can be given a real structure: none, a real structure (a conjugation $K$ with $K^2=1$), and a quaternionic structure (an antiunitary $J$ with $J^2=-1$). Only the last enforces a degeneracy, and the reason is the one the proof exhibits: $J^2=-1$ is what makes the partner orthogonal to its source, whereas a real structure's partner is not orthogonal to it in general and no degeneracy follows. The opposite-sign verification above is the second row of the table realized: a real symmetric matrix has no enforced degeneracy.

The biquaternion reading is that the algebra contains the units for exactly the third row and the involutions for the second. Its three imaginary elements $e_k$ square to $-e_0$ and supply candidate $J$'s; its involutions $^*$, $\dagger$, $\flat$ have fixed spaces of real dimensions $4,4,4$ and supply real structures, though as the mass article insists, an *algebra* involution is not yet a *module* conjugation. The unitary class is the absence of any such structure, and it is the generic class in the sense that a perturbation breaking the antiunitary symmetry removes the degeneracy without restoring it.

## What Breaks the Symmetry

**A magnetic field.** The standard $\mathcal T$-odd perturbation of a spin system is a term linear in an external field,

$$
H_{\text{field}}=-\boldsymbol\mu\cdot\mathbf B ,
\qquad
\boldsymbol\mu=\gamma\mathbf S ,
$$

and it breaks the symmetry because the angular momentum is $\mathcal T$-odd while the field is $\mathcal T$-invariant. In the module language the perturbation is a term along a chosen axis, and the axis is one of the three imaginary directions of the algebra: the field singles out a unit $n$ and hence a particular $e_n$, and the pair $\{v,\mathcal Tv\}$ is split by an amount proportional to the field. This is the empirical signature of the classification: a Kramers pair's splitting in a field is the statement that no $\mathcal T$-invariant perturbation can lift it.

**The linear splitting, and why it is linear.** The two facts — an invariant perturbation cannot split a pair, an odd one splits it linearly — follow from the transformation of the perturbation. Under $\mathcal T$ the spin operators are odd,

$$
\mathcal T\sigma^\alpha\mathcal T^{-1}=-\sigma^\alpha ,
\qquad \alpha=x,y,z ,
\qquad
\mathcal T\,I\,\mathcal T^{-1}=I ,
$$

verified with residuals $0$. In the Kramers basis $\{v,\mathcal Tv\}$ an invariant perturbation therefore has equal diagonal matrix elements and does not split the pair, while a term proportional to a spin component has opposite diagonal elements and splits it to first order. The behaviour was computed on the four-dimensional model above: with the orbital part $h=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ and a spin term of strength $b$,

$$
\begin{aligned}
b=0:\quad &\text{spectrum } \{-1,-1,3,3\}\ \text{(Kramers pairs)},\\
b=0.01:\quad &\text{spectrum } \{-1.01,-0.99,2.99,3.01\},\\
b=0.02:\quad &\text{spectrum } \{-1.02,-0.98,2.98,3.02\},
\end{aligned}
$$

a splitting of exactly $2b$ per pair and linear in the field, while a $\mathcal T$-even perturbation of the same strength leaves the spectrum $\{-1.01,-1.01,3.01,3.01\}$ — shifted and still degenerate. The linear splitting of a Kramers pair in a magnetic field is the theorem's quantitative face.

**The framework's standing disclaimer.** The algebra can say *which* perturbations break the symmetry — those containing an odd number of imaginary units along a chosen axis, in the material sector — and it can say that the symmetry's sign is the covering element $-e_0$. It cannot choose the axis, and it cannot assign a magnitude. The position matches the one the path-integral companion records for the $i\epsilon$ and the mass article records for the two masses: the algebra names the axis, the boundary or empirical data choose its orientation.

**Relation to the other discrete symmetries.** Charge conjugation, parity and their combination are treated by the companion articles *The Reflection and the Rotation in Biquaternionic Form* and *The CPT Theorem in Biquaternionic Form*, and are not the subject here. What matters for Kramers is only that $\mathcal T$ be antiunitary and square to $-e_0$; the other symmetries may or may not be present, and the degeneracy survives on the strength of $\mathcal T$ alone.

## What Is Standard and What the Algebra's

**Standard, transcribed.** Antiunitarity, the decomposition $\mathcal T=UK$, the theorem $\mathcal T^2=(-1)^{2s}$, Kramers' theorem and its proof, the Kramers doublet and its splitting in a magnetic field, and the quaternionic structure of a Hilbert space with an antiunitary $J$ squaring to $-1$. All standard, in the parents' conventions.

**The algebra's own.**

- *The sign as the covering element.* $\mathcal T^2=UU^*=U^2=-e_0$ for the spinor, with $U=n\cdot e$ the real rotation element; the same $-e_0$ is the $2\pi$ rotor of the spin–statistics companion. Kramers degeneracy and the fermionic $2\pi$ phase are the same algebra fact.
- *The three imaginary units as the axes.* $\mathbb{B}$'s imaginary elements are the candidate $J$'s; the realization is the module's, as the mass article insists, and the algebra's contribution to $\mathcal T$ is the sign and the axis set.

**Open.**

- **The module-level conjugation.** The construction uses a module conjugation $K$ realizing the algebra's $^*$; the companion article on antilinear structure is explicit that the algebra's real structure and the module's real structure are different maps, and the explicit rendering of $K$ on the module is not fixed here.
- **Finite versus infinite dimension.** The proof and the verification are finite-dimensional. The theorem holds in infinite dimensions, but the framework's finite-algebra formulas do not by themselves extend it.
- **Magnitudes.** The algebra gives the degeneracy parity and the axes, and no scale; the size of a Kramers splitting is empirical, as the mass article says of the masses.

## Companion Articles

- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the three antilinear involutions, the real structure $\flat$, and the distinction between the algebra's and the module's real structures that this article inherits.
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin generators $\tilde S_k=\tfrac{\hbar}{2}ie_k$ and the module action on which time reversal is constructed.

## Summary

Kramers degeneracy in biquaternion form is the antiunitary symmetry $\mathcal T=UK$ of the spin-$\tfrac12$ module whose square is the $2\pi$ rotor: with $U=n\cdot e$ the real rotation element ($U^*=U$, $(n\cdot e)^2=-e_0$),

$$
\mathcal T^2=U U^*=U^2=-e_0=R(2\pi) ,
$$

so that $\mathcal T^2=(-1)^{2s}e_0$ is the covering sign that the spin–statistics companion also uses. The algebra supplies the sign and the set of axes $\{e_1,e_2,e_3\}$; the module supplies the conjugation, in the same algebra-versus-module division that the mass article enforces.

The theorem follows from antiunitarity alone: if $[\mathcal T,H]=0$ and $\mathcal T^2=-1$, the partner $\mathcal Tv$ of every eigenvector $v$ is degenerate ($[\mathcal T,H]=0$) and orthogonal ($\langle\mathcal Tv,v\rangle=-\overline{\langle v,\mathcal Tv\rangle}$), so every level is even-degenerate. All of it was recomputed: for $\mathcal T=i\sigma_yK$, $U$ real with $U^2=-I_2$, $\mathcal T^2=-1$, antiunitarity with error $0$, and $\langle\mathcal Tv,v\rangle=0$ for random $v$; on $\mathbb{C}^4$ a $[\mathcal T,H]=0$ model with $H=I_2\otimes h$, $h=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ has the doubly degenerate pair $\{v,\mathcal Tv\}$ at $E=3$ with residuals $0$; a random real symmetric $H$ (the $\mathcal T^2=+1$ case) has four distinct levels, $\{-3.01553,-1.70328,0.12807,2.44612\}$, with minimum gap $1.31225$.

The same antiunitary $J$ with $J^2=-e_0$ is a quaternionic structure, and the commutant of $\mathcal T$ on $\mathbb{C}^2$ was computed to be two-complex-dimensional — the quaternionic line. The counting of invariant Hamiltonians follows: on $\mathbb{C}^{2N}$ a $\mathcal T$-invariant Hermitian operator has block form $H=\begin{pmatrix}A&B\\-B^*&A^*\end{pmatrix}$ with $A=A^\dagger$, $B=-B^T$ and real dimension $N(2N-1)$ — $(1,6,15)$ for $N=1,2,3$, against $4N^2$ for a general Hermitian operator, with the constraint of rank $N(2N+1)$. The three symmetry classes are $\mathcal T^2$ absent, $+e_0$ (orthogonal, real) and $-e_0$ (symplectic, quaternionic), and only the last enforces degeneracy. A magnetic field, a term along a chosen imaginary direction, is what breaks the symmetry, and the framework's verdict is the familiar one: the algebra names the axis and does not choose it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal T=UK$ | Antiunitary time reversal; $U$ unitary, $K$ antilinear involution |
| $\langle\mathcal Tu,\mathcal Tv\rangle=\overline{\langle u,v\rangle}$ | Antiunitarity |
| $U=\exp(\tfrac{\pi}{2}n\cdot e)=n\cdot e$ | $\pi$-rotation element; $(n\cdot e)^2=-e_0$, $U^*=U$ |
| $\mathcal T^2=UU^*=U^2=-e_0$ | Kramers sign as the covering element |
| $R(2\pi)=\exp(\pi n\cdot e)=-e_0$ | The $2\pi$ rotor (spin–statistics companion) |
| $\mathcal T^2=(-1)^{2s}e_0$ | Sign by spin: $-1$ half-integer, $+1$ integer |
| $\mathcal T=i\sigma_yK$ | Standard spinor representative; $U$ real, $U^2=-I_2$ |
| $\{v,\mathcal Tv\}$ | Kramers doublet (degenerate, orthogonal pair) |
| $\langle\mathcal Tv,v\rangle=0$, $H(\mathcal Tv)=E(\mathcal Tv)$ | Proof identities (recomputed, error $0$) |
| $H_{\text{field}}=-\boldsymbol\mu\cdot\mathbf B$ | $\mathcal T$-odd perturbation; lifts the degeneracy |
| $\tilde Q^*,\tilde Q^\dagger,\tilde Q^\flat=-\tilde Q^\dagger$ | The algebra's three antilinear involutions (companion) |
| $\flat=+$ on $\mathbb{M}_-$, $- $ on $\mathbb{M}_+$ | Sector action of the algebra's real structure |
| $J^2=-e_0$, $J=UK$ | Quaternionic structure of the state space |
| $\dim_\mathbb{C}\{M:[\mathcal T,M]=0\}=2$ | Quaternionic line; commutant computed by rank |
| $e_1,e_2,e_3$ | The three imaginary units = the three candidate axes |
| $H=\begin{pmatrix}A&B\\-B^*&A^*\end{pmatrix}$, $A=A^\dagger$, $B=-B^T$ | $\mathcal T$-invariant Hermitian form on $\mathbb{C}^{2N}$ |
| $\dim_\mathbb{R}\{H\text{ invariant}\}=N(2N-1)$ | Counting against $4N^2$ for general Hermitian |
| $\mathcal T^2$ absent / $+e_0$ / $-e_0$ | Unitary / orthogonal / symplectic class |

## Further Reading

- H. A. Kramers, "Théorie générale de la rotation paramagnétique dans les cristaux," *Proceedings of the Royal Academy of Amsterdam* **33** (1930) 959–972, for the degeneracy theorem.
- E. P. Wigner, *Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra* (Academic Press, 1959), for antiunitary operators, time reversal and the sign $\mathcal T^2=(-1)^{2s}$.
- A. Messiah, *Quantum Mechanics*, Vol. 2 (North-Holland, 1962), for the Kramers theorem, its proof, and the magnetic-field splitting of a Kramers pair.
- J. J. Sakurai, *Modern Quantum Mechanics* (Addison-Wesley, 1994), for the antiunitary time-reversal operator and its representation.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic structure of a Hilbert space with an antiunitary $J$, $J^2=-1$, and its physical consequences.
- C. L. Kane and E. J. Mele, "Quantum spin Hall effect in graphene," *Physical Review Letters* **95** (2005) 226801, and J. E. Moore, "The birth of topological insulators," *Nature* **464** (2010) 194–198, for Kramers degeneracy and its topological protection.
- B. A. Bernevig and T. L. Hughes, *Topological Insulators and Topological Superconductors* (Princeton, 2013), for time reversal, Kramers pairs, and the $\mathbb{Z}_2$ classification.
- F. Haake, *Quantum Signatures of Chaos* (Springer, 2010), for the three symmetry classes (unitary, orthogonal, symplectic) selected by $\mathcal T^2=0,\pm1$.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the conjugation involutions of the biquaternion/Clifford algebra and their fixed spaces.
