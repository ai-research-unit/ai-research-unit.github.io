# __The Dirac Pair and the Mass Term__

## Introduction

A single Weyl spinor is a spin-$\tfrac12$ field of one chirality. It cannot carry a mass, because a mass term pairs the field with a second field and a single spinor has no second field to pair with. The Dirac spinor is that second field added: the direct sum of the two inequivalent spinor representations, of complex dimension four, and the mass is the bilinear that couples the two halves.

This article states the two Weyl spinors and their actions, forms the Dirac pair, shows why the mass term couples the halves and why the coupling is a parity-respecting bilinear, fixes the chirality grading and its relation to helicity, and states the Majorana option and the sense in which it is a different pairing.

The article assumes *The Two Commuting Complex Triples* and *P, T and the Representation Labels* for the representation labels, *The 2×2 Matrix Model: What It Computes and What It Cannot Show* for the algebra acting on a spinor, and the corpus's field articles for the equations. It does not restate the corpus's conventions for the spinor module, which are fixed in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; the mass's algebraic shape is settled in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, and this article defers to it.

## The Two Weyl Spinors

### The Two Inequivalent Representations

The two spinor representations of the Lorentz algebra are

$$
(\tfrac12,0)\ \text{and}\ (0,\tfrac12),
$$

both of complex dimension two, and they are **inequivalent**: no change of basis takes one to the other. They are conjugate to one another, so complex conjugation exchanges them, and that exchange is what parity does.

### The Two Actions

On the first, the generators act by left multiplication in the corpus's matrix model, $\vec e_k\mapsto-i\sigma_k$ for the rotations and $i\vec e_k\mapsto\sigma_k$ for the boosts, as *The Spinor Representation of the Lorentz Group in Biquaternionic Form* fixes them; multiplied by $\tfrac{i}{2}$ the same two read $\tfrac12\sigma_k$ and $\tfrac{i}{2}\sigma_k$, the normalisation in which the rotation generator is Hermitian and the boost generator carries the $i$. On the second the sign of the boost part is reversed relative to the rotation part. So the two spinors differ by the sign of the boost, which is the statement that they are conjugate representations and not equivalent ones.

In the algebra, the first is the defining module $V_{1/2}=\mathbb{C}^{2}$ and the second is its conjugate $\overline{V_{1/2}}$. The algebra acts on the first by left multiplication, and the second is reached by complex conjugation. The corpus reserves the bar for complex conjugation and the star for the Hermitian conjugation built from it, and the exchange of the two chiralities on the module is what the corpus calls charge conjugation there; this article keeps the names apart and writes "complex conjugation" when it means the bar.

### Why Two and Not One

A single Weyl spinor is a perfectly good representation. What it is not is a representation that contains its own conjugate, so a term pairing it with itself is not available without an extra structure. That is the whole reason the framework carries a **pair**: not because one spinor is insufficient to describe a massless particle, but because a mass needs two.

### The Corpus's Statement

The survey states the point in one sentence: the framework carries a Dirac pair rather than a single Weyl spinor, and the mass term couples the two chiralities. This article is the working out of that sentence.

## The Dirac Spinor as a Pair

### The Direct Sum

$$
\Psi=\begin{pmatrix}\xi\\ \eta\end{pmatrix},
\qquad
\xi\in(\tfrac12,0),\quad \eta\in(0,\tfrac12),
$$

of complex dimension $2+2=4$. The direct sum is a representation, and it is the smallest representation that contains both chiralities.

### The Algebra's Version

The Dirac spinor is also an element of the algebra itself:

$$
\mathbb{B}\cong M_2(\mathbb{C})\cong\mathbb{C}^{2}\otimes\mathbb{C}^{2*}\cong\mathbb{C}^{4},
$$

so the four complex dimensions of the algebra are the four of the Dirac spinor. In that reading $\xi$ is the column index and $\eta$ the row index, and the two chiralities are the two tensor factors' transformations. That is why the algebra's regular representation is Dirac and not Weyl.

### The Dirac Matrices

In the chiral basis the matrices are built from the two off-diagonal blocks,

$$
\gamma_{0}=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\gamma_k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix},
$$

with the $2\times2$ blocks acting on the two spinors. The chiral basis is the one in which the grading is diagonal, and it is the basis adapted to the pair.

### The Verification

The chiral algebra is checked directly: $\{\gamma_5,\gamma_{\imath}\}=0$ for all four $\mu$, $\gamma^{5\,2}=1$, and $\gamma^{5}$ is diagonal with eigenvalues $(-1,-1,+1,+1)$ — the upper block of $\Psi$ carrying $-1$ and the lower block $+1$ in the convention of this article. All three statements hold exactly in the $4\times4$ realisation.

## The Mass Term

### The Coupling

$$
m\,\Psi^{\dagger}\gamma_{0}\Psi
=m\bigl(\xi^{\dagger}\eta+\eta^{\dagger}\xi\bigr)
=2m\,\mathrm{Re}\bigl(\xi^{\dagger}\eta\bigr).
$$

The bilinear is off-diagonal in the two halves: it pairs $\xi$ with $\eta$ and $\eta$ with $\xi$, and it never pairs a half with itself. The verification: with $\xi=(1,0)$ and $\eta=(0.3+0.2i,0.5)$ the bilinear $\Psi^{\dagger}\gamma_{0}\Psi$ is $0.600000000$, and $2\mathrm{Re}(\xi^{\dagger}\eta)$ is $0.600000000$.

So the mass is a **coupling** and not a self-energy: it has no diagonal part at all.

### Why Parity Allows It

Parity exchanges the two chiralities, so a bilinear that pairs them is parity-invariant, while a bilinear that paired one with itself would not be. That is the group-theoretic reason a Dirac mass is allowed: the term is a singlet of the full Lorentz group including parity, and it is built from one field of each chirality.

The converse is the reason a *single* Weyl spinor cannot have a Dirac mass: there is no second chirality in the field content to pair with, and the only available self-pairing is the antilinear one of the Majorana option.

### The Two Equations

The coupled system in the corpus's notation is

$$
\tilde\nabla_\Phi\tilde\Xi_R=2\pi\nu_m\tilde\Xi_L,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=2\pi\nu_m\tilde\Xi_R,
$$

with $\nu_m=\frac{mc}{h}$ the mass wave number. Each equation is first order and each carries the other chirality on its right-hand side: the mass is the term that converts one into the other as the field propagates.

That is the algebraic form of "a massive particle's chirality flips as it moves": the free equation is a rotation of the pair, and its rate is $\nu_m$.

### The Mass as a Frequency

The mass wave number is the frequency of that rotation, and the rotation's period is the Compton wavelength. So the mass is not a coupling constant in the usual sense but a *rate*: a massless field's two halves propagate independently, and a massive field's two halves rotate into each other with a fixed frequency. In the massless limit the frequency goes to zero and the two halves decouple.

### What the Mass Is Not

It is not a deformation of either half and it is not a fifth component. It is a bilinear in the pair, and its value is empirical: the framework does not derive it, as the corpus's article on the two kinds of mass states plainly.

## Chirality

### The Projectors

$$
P_{\pm}=\tfrac12\bigl(1\pm\gamma^{5}\bigr),
\qquad
P_{\pm}^{2}=P_{\pm},\quad P_{+}P_{-}=0,\quad P_{+}+P_{-}=1,
$$

and

$$
P_{+}\Psi=\begin{pmatrix}0\\ \eta\end{pmatrix},
\qquad
P_{-}\Psi=\begin{pmatrix}\xi\\ 0\end{pmatrix}
$$

in the convention above. The projectors are the chirality projectors, and their eigenvalues $\pm1$ are the chirality.

### Chirality and Helicity

Chirality is a property of the representation; helicity is the projection of the spin on the momentum. For a **massless** particle they coincide, because the momentum is null and the little group's rotation is the same as the chirality's generator. For a **massive** particle they do not: a boost can overtake the spin, and the helicity flips while the chirality does not.

That is why the two words must not be used interchangeably, and why the block's statement "the mass couples the two chiralities" is stronger than "the mass couples the two helicities".

### The Massless Limit

As $\nu_m\to0$ the two equations decouple:

$$
\tilde\nabla_\Phi\tilde\Xi_R=0,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=0,
$$

and each half is separately a good field. So the Weyl spinors are the massless limit of the pair, and the pair is the massive completion. The limit is continuous in the equations and discontinuous in the particle content: a massless particle has one helicity, a massive one has two.

### The Particle Content

A Dirac field describes two spin states of a particle and two of its antiparticle, and the mass does not change that count. What the mass changes is the *identity* of the states: a massive particle's spin can be oriented either way about its momentum, while a massless one's cannot be flipped without changing its chirality. So the count of states is the same at every mass and the labels of the states are not.

## The Majorana Option

### The Antilinear Condition

A Majorana spinor is one that equals its own charge conjugate:

$$
\Psi=\Psi_{c},
$$

which is a **reality condition** and therefore antilinear. It reduces the four complex components to four real ones, and it is available only when the conjugation is an involution on the field's space and commutes with the equation.

### What It Buys

With the condition imposed, the mass term becomes a self-pairing: the field is paired with its own conjugate, and no second field is needed. So a Majorana mass is possible for a single Weyl spinor, and that is the option the Dirac mass does not have.

The corpus's precise statement is that the **Dirac mass is linear** and pairs no field with its own conjugate, while the **Majorana mass is antilinear** and pairs a field with its own conjugate, and that the Majorana condition's reality space is four real dimensional and preserves the mass shell. So the Majorana option is physical and not a formal curiosity.

### Why Both Options Exist

Both exist because the algebra carries more than one conjugation. The linear one gives the Dirac pairing of two halves; the antilinear ones give the self-pairing. Which one a given fermion uses is empirical — the neutrino is the case where the question is open — and the framework supplies the algebraic distinction without deciding the assignment.

That is the honest boundary, and the corpus draws it explicitly: the framework does not derive the masses and does not decide which kind a given fermion carries.

### The Caution

The corpus's article on the two kinds of mass records an algebra-level equation that uses the algebra's real structure as though it were a mass on the module, and it records that the equation fails on the dispersion relation. The lesson is that the two real structures live on different spaces: the algebra's and the module's. This article therefore states the Majorana condition as a condition on the module and does not import the algebra's involution into it.

## Where the Equation Goes

This article stops at the carrier and the coupling. The equation itself — the plane-wave solutions, the spin sums, the non-relativistic reduction and the interpretation of the four components — is *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*, which takes the pair and the mass term proved here as its starting point. The division is deliberate: what is representation theory belongs here, and what is a computation with solutions belongs there.

## Summary

A Weyl spinor is one chirality; the Dirac spinor is the direct sum of the two inequivalent spinor representations and is, in the algebra, the algebra itself as a four-dimensional complex space. The mass term is the off-diagonal bilinear $m\Psi^{\dagger}\gamma_{0}\Psi=2m\mathrm{Re}(\xi^{\dagger}\eta)$, verified to vanish on the diagonal and to pair the two halves, and it is parity-allowed because parity exchanges the halves. In the field equations the mass is the rate at which one chirality converts into the other, with frequency $\nu_m=\frac{mc}{h}$, and the massless limit decouples the two. Chirality is the $\gamma^{5}$ eigenvalue and coincides with helicity only for a massless particle. The Majorana option is the antilinear self-pairing, available for a single Weyl spinor and physically realised, and it is a different pairing from the Dirac one, built on a different real structure.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\xi\in(\tfrac12,0)$, $\eta\in(0,\tfrac12)$ | the two Weyl spinors |
| $\Psi=(\xi,\eta)$ | the Dirac pair |
| $\gamma^{5}$ | the chirality grading, $\mathrm{diag}(-1,-1,+1,+1)$ |
| $P_{\pm}=\tfrac12(1\pm\gamma^{5})$ | the chirality projectors |
| $\nu_m=\frac{mc}{h}$ | the mass wave number |
| $\Psi_{c}$ | the charge conjugate |

## Further Reading

- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §5.4–5.5 — the Dirac and Majorana masses and their reality conditions.
- P. B. Pal, "Dirac, Majorana and Weyl fermions", *American Journal of Physics* 79 (2011) 485 — the three options and the relations between them.
- *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* — the corpus's separation of the Dirac and Majorana pairings.
- *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form* — the conjugation that the Majorana condition uses.
- *Chiral Fermions in the Biquaternion Framework* — chirality in the algebra's own terms.
- *P, T and the Representation Labels* — the exchange of the two spinor representations under parity.
- *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* — the equation, its solutions and the non-relativistic reduction, which take this article's pair and mass term as their starting point.
