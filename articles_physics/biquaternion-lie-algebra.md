# __Biquaternion Lie Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries a natural bracket, the commutator, and with it the structure of a Lie algebra. This article reads that structure: the algebra as the Lie algebra of the group of units, its centre, the trace-free subalgebra, the derived subalgebra and its identity with the vector subspace, the bracket of two vectors as a cross product, the action of the bracket on the six distinguished subspaces, and the real form of the trace-free part with its two three-dimensional real summands. The adjoint maps close the account as the infinitesimal automorphisms.

The metric identification of the trace-free part with the Lorentz algebra, and of the group it exponentiates to with the spin group of Lorentzian signature, is *Biquaternion Lie Group and Exponential Structure* and *Biquaternion Rotations and Lorentz Transformations*; it is metric and is not made here. The topology of the group is *The Biquaternion Unit Group as a Topological Group*, and the automorphisms are *Biquaternion Automorphisms and Derivations*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$. The six distinguished subspaces are those of *Biquaternion Algebra* and *Relations Between Subspaces*.

## The Algebra as a Lie Algebra

The trace functional is $\mathrm{Tr}(\tilde{Q})=2Q_0$. The set $\mathbb{B}$ carries the **commutator bracket**

$$
[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P},
$$

under which it is a complex Lie algebra, written $\mathrm{G}$, of dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$. Its centre is the scalar line

$$
\mathrm{Z}(\mathrm{G})=\mathbb{C}e_0,
$$

of complex dimension $1$ and real dimension $2$; every scalar multiple of $e_0$ commutes with all of $\mathbb{B}$. Removing the centre gives the decomposition

$$
\mathrm{G}=\mathrm{B}_0\oplus\mathbb{C}e_0,
$$

with complex dimensions $4=3+1$ and real dimensions $8=6+2$, where

$$
\mathrm{B}_0=\{\tilde{Q}\in\mathbb{B} : Q_0=0\}=\mathrm{span}_\mathbb{C}\{e_1,e_2,e_3\}
$$

is the **trace-free subalgebra**, the complex pure-vector part.

**Physical reading.** $\mathrm{G}$ is the Lie algebra of the group of units, which is $\mathrm{GL}(2,\mathbb{C})$ over $\mathbb{C}$; the centre $\mathbb{C}e_0$ is the generator of the central phase, the one direction that commutes with everything and therefore the one direction that cannot be gauged away by the algebra's own action. In physics terms the centre is the global phase generator, and the trace-free part is where the non-abelian content of the framework lives. The centre is also the scalar line of the physical dictionary: a general element carries $ct'+ict$ on its scalar coefficient, the real part the informational time and the imaginary part the material time, so the complex line $\mathbb{C}e_0$ is where both sectors put their time.

## The Trace-Free Subalgebra

The Lie algebra of the norm-one group is the trace-free subalgebra

$$
\mathrm{B}_0=\{\tilde{Q}\in\mathbb{B} : Q_0=0\}=\mathrm{span}_\mathbb{C}\{e_1,e_2,e_3\},
$$

of complex dimension $3$ and real dimension $6$, closed under the bracket $[e_j,e_k]=2\sum_l\epsilon_{jkl}e_l$. Over the reals it splits into two three-dimensional real subspaces,

$$
\mathrm{B}_0=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\;\oplus\;\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\},
$$

with real dimensions $6=3+3$. The first summand is the **rotation subalgebra**

$$
\mathrm{K}=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\},
$$

the Lie algebra of the rotation directions, on which the bracket is twice the cross product; the second, $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$, consists of the **hyperbolic-rotation directions**, the boosts. The two are non-isomorphic real Lie algebras; which of them is compact is a topological statement, made in *The Biquaternion Unit Group as a Topological Group*.

In the fixed-point subspaces the rotation directions are $e_k\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$ and the hyperbolic-rotation directions are $ie_k\in\mathbb{M}_+$. This is why pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ while pure boosts have rotors in $\mathbb{M}_+$: these are exactly the two real three-dimensional pieces into which $\mathrm{B}_0$ splits, and they are the infinitesimal generators of the two kinds of motion.

**Physical reading.** The split $\mathrm{B}_0=\mathrm{K}\oplus\mathrm{span}_\mathbb{R}\{ie_k\}$ is the split of the Lorentz algebra into **rotations and boosts**: $\mathrm{K}$ is the rotation generator $\mathbf{J}$, with the compact bracket $[J_i,J_j]=\epsilon_{ijk}J_k$ up to the factor two, and the hyperbolic directions are the boost generator $\mathbf{K}$. The boost directions are non-compact and their bracket closes on the rotations, $[K_i,K_j]\propto-\epsilon_{ijk}J_k$, which is the statement that two boosts compose to a rotation; the two pieces are therefore not isomorphic, and neither is an ideal of the other. The two kinds of generator differ in the square of the direction and in what they move: a rotation direction $e_k$ has $e_k^2=-e_0$ and a spacelike plane, while a boost direction $ie_k$ has $(ie_k)^2=+e_0$ and a timelike one. On the material four-position $\tilde{Q}=ict\,e_0+\mathbf{x}$ the rotation acts by rotating $\mathbf{x}$ and leaving the time slot $ict$ alone, and the boost acts by mixing the time slot with the spatial slot $x_k$. A boost is therefore a rotation by an **imaginary angle** in a plane that contains the time direction: the rotation angle $\theta$ of such a plane is $i\psi$ for a boost, with $\psi$ the rapidity. This is the algebraic content of the $ict$ convention, and it is why the boost rotor lies in $\mathbb{M}_+$ while the rotation rotor lies in $\mathbb{H}_{\mathbb{B}}$. The metric that turns this bracket into the Lorentz bracket is imposed in *Biquaternion Lie Group and Exponential Structure*, and here it is only the split that is claimed.

## The Derived Subalgebra, the Cross Product and the Subspaces

The commutator of two biquaternions has vanishing scalar part, since the scalar part commutes with everything, $[\tilde{P},\tilde{Q}]=[\mathbf{P},\mathbf{Q}]$, and the bracket of the basis vectors is $[e_j,e_k]=2\sum_l\epsilon_{jkl}e_l$. Hence the **derived subalgebra** is the complex span of the vector units,

$$
[\mathrm{G},\mathrm{G}]=\mathrm{B}_0=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}=\mathrm{Vect}(\mathbb{B}),
$$

of complex dimension $3$ and real dimension $6$: the derived subalgebra is exactly the vector subspace, and the quotient $\mathrm{G}/[\mathrm{G},\mathrm{G}]$ is the centre $\mathbb{C}e_0$.

For two pure vectors the quaternion product splits into its scalar and vector parts, $\mathbf{P}\mathbf{Q}=-(\sum_kP_kQ_k)e_0+\mathbf{P}\times\mathbf{Q}$, so the bracket is **twice the cross product**,

$$
[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\times\mathbf{Q},
$$

with the cross product taken in $\mathbb{C}^3$ under $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$. The map $\mathbf{P}\mapsto\operatorname{ad}_{\mathbf{P}}|_{\mathrm{B}_0}$ is then the cross-product operator, and for a real vector part it is the antisymmetric map represented by a real antisymmetric $3\times3$ matrix.

The action of the bracket on each of the six distinguished subspaces — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ — is the commutator row of the tables of *Relations Between Subspaces*. In brief, the centre is central, $\mathrm{Vect}(\mathbb{B})$ is closed and the bracket on it is the cross product above, $\mathbb{H}_{\mathbb{B}}$ is closed with the bracket of the imaginary quaternions, the bracket carries $\mathbb{M}_+$ to $\mathbb{M}_-$ and $\mathbb{M}_-$ to itself, and the bracket of $\mathbb{M}_+$ with $\mathbb{M}_-$ carries the second back to the first.

**Physical reading.** $[\tilde{P},\tilde{Q}]=2\,\mathbf{P}\times\mathbf{Q}$ is the **commutator of the angular momentum operators**: the algebra of rotations is the cross-product algebra, and the factor two is the factor that the half-angle of the rotor carries. That the derived subalgebra is the whole trace-free part says the algebra is not solvable and has no abelian ideal beyond the phase, so the framework's symmetry is semisimple up to the central $U(1)$ — the algebraic reason its gauge structure has no free abelian factor beyond the phase.

## The Real Structure and the Adjoint Maps

Over $\mathbb{R}$ the algebra is the Lie algebra of the real Lie group $\mathbb{B}^\times$, and the trace-free part $\mathrm{B}_0$, of real dimension $6$, is its real form, with $[\mathrm{G},\mathrm{G}]=\mathrm{B}_0$ as over $\mathbb{C}$. The identification of $\mathrm{B}_0$ with the Lorentz algebra, and of the group it exponentiates to with the spin group of Lorentzian signature, is metric: it is made in *Biquaternion Lie Group and Exponential Structure* and *The Biquaternion Unit Group as a Topological Group*, along with *Biquaternion Rotations and Lorentz Transformations*.

The **adjoint maps** are the inner derivations

$$
\operatorname{ad}_{\tilde{Q}}:X\mapsto[\tilde{Q},X],
$$

each a derivation of the algebra by the Jacobi identity, and $\tilde{Q}\mapsto\operatorname{ad}_{\tilde{Q}}$ is a Lie algebra homomorphism with kernel the centre $\mathbb{C}e_0$. Since $\mathbb{B}$ is simple, every derivation is inner, so

$$
\operatorname{Der}(\mathbb{B})=\operatorname{ad}(\mathbb{B})\cong\mathrm{G}/\mathrm{Z}(\mathrm{G})=\mathrm{SL}(2,\mathbb{C}),
$$

the derivations are the infinitesimal automorphisms of the algebra, of complex dimension $3$ and real dimension $6$, and they exponentiate to the inner automorphisms $\operatorname{Inn}(\mathbb{B})=\mathbb{B}^\times/\mathbb{C}^\times$ (*Biquaternion Automorphisms and Derivations*).

**Physical reading.** The adjoint map $\operatorname{ad}_{\tilde{Q}}$ is the infinitesimal transformation of the algebra under the motion generated by $\tilde{Q}$; that the derivations are exactly the inner ones is the statement that every infinitesimal symmetry of the framework is generated by an element of the algebra, and hence acts in the defining module. It is why the framework has no infinitesimal symmetry that fails to be a motion.

## Summary

The biquaternion algebra, with the commutator bracket, is the complex Lie algebra $\mathrm{G}$ of complex dimension $4$ and real dimension $8$, with centre $\mathbb{C}e_0$ and trace-free part $\mathrm{B}_0=\mathrm{span}_\mathbb{C}\{e_1,e_2,e_3\}$ of complex dimension $3$ and real dimension $6$. The derived subalgebra is the vector subspace itself, $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$, so the algebra is not solvable; the bracket of two pure vectors is twice their cross product. Over $\mathbb{R}$ the trace-free part splits into the rotation subalgebra $\mathrm{K}=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, on which the bracket is twice the cross product, and the hyperbolic directions $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$; these are the infinitesimal rotations and boosts, and the metric identification of the real form with the Lorentz algebra is made in the Lie-group article. The derivations are exactly the inner ones, $\operatorname{Der}(\mathbb{B})=\operatorname{ad}(\mathbb{B})\cong\mathrm{SL}(2,\mathbb{C})$, exponentiating to $\operatorname{Inn}(\mathbb{B})=\mathbb{B}^\times/\mathbb{C}^\times$. In the $ict$ convention the split of $\mathrm{B}_0$ is the algebraic origin of the two motions of the material four-position $\tilde{Q}=ict\,e_0+\mathbf{x}$: the rotation directions rotate $\mathbf{x}$ and leave the time slot $ict$ fixed, the boost directions $ie_k$, of square $+e_0$, mix $ict$ with $x_k$, and a boost is a rotation by the imaginary angle $i\psi$ in that plane.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G}$ | $\mathbb{B}$ as a Lie algebra with the commutator; complex dim $4$, real dim $8$ |
| $\mathrm{Z}(\mathrm{G})=\mathbb{C}e_0$ | Centre; the phase generator |
| $\mathrm{B}_0=\mathrm{span}_\mathbb{C}\{e_1,e_2,e_3\}$ | Trace-free subalgebra; complex dim $3$, real dim $6$ |
| $\mathrm{K}=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ | Rotation subalgebra; the generator $\mathbf{J}$ |
| $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$ | Hyperbolic-rotation directions; the boost generator $\mathbf{K}$ |
| $e_k^2=-e_0$, $(ie_k)^2=+e_0$ | Spacelike rotation plane and timelike boost plane |
| $\tilde{Q}=ict\,e_0+\mathbf{x}$ | Material four-position; the scalar slot is the time $ict$, the vector slots the space $\mathbf{x}$ |
| $[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\times\mathbf{Q}$ | Bracket of two pure vectors, twice the cross product |
| $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$ | Derived subalgebra is the vector subspace |
| $\operatorname{ad}_{\tilde{Q}}=[\tilde{Q},\cdot]$ | Adjoint maps; the inner derivations |
| $\operatorname{Der}(\mathbb{B})\cong\mathrm{SL}(2,\mathbb{C})$ | All derivations are inner |
| $\operatorname{Inn}(\mathbb{B})=\mathbb{B}^\times/\mathbb{C}^\times$ | Inner automorphisms |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the commutator algebra of an associative algebra, the derived subalgebra and the inner derivations.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $\mathfrak{sl}(2,\mathbb{C})$, its real forms and the rotation and boost generators.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the commutator, the cross product of the vector parts and the six subspaces.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lie algebra of the spin and Lorentz groups and its real forms.
- *The Lorentz Transformation as a Biquaternionic Rotation* (`articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.md`), for the boost biquaternion, the rapidity as an imaginary rotation angle and the rotor conjugation that realises the boost reading used here, and *The Four-Vector Representation of Biquaternions* (`articles_physics/the-four-vector-representation-of-biquaternions.md`), for the material and informational coordinate forms $ict\,e_0+\mathbf{x}$ and $ct'\,e_0+i\mathbf{x}'$.
