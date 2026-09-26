# __The ADHM Construction and Biquaternion Instanton Data__

## Introduction

*Instantons and Solitons in Biquaternionic Form* exhibited the BPST instanton as an explicit solution of the self-duality equation inside the compact factor $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}\subset\mathbb M_-$, fixed its charge and action, and recorded its moduli. *The Index Theorem and the Zero-Mode Count in Biquaternionic Form* counted the fermion zero modes that the instanton supports. Neither article says where the instanton's **data** comes from, or why a first-order self-duality equation should have any solutions at all beyond the one written down by hand. This article supplies that missing layer: the Atiyah–Drinfeld–Hitchin–Manin (ADHM) construction, which parametrises *all* self-dual connections on the Euclidean slice by a finite set of matrices satisfying two algebraic equations.

The ADHM construction is unusual among the results of gauge theory in that its natural language is already the language of the framework. The self-duality equation on $\mathbb R^4$ is a *quaternionic* equation: $\mathbb R^4$ is identified with the real-quaternion subspace $\mathbb H_{\mathbb B}$, the four-dimensional rotation group is $SU(2)\times SU(2)$ acting by left and right quaternion multiplication, and a self-dual curvature is one whose components are holomorphic with respect to the quaternionic structure. The ADHM theorem states that the moduli space of self-dual connections on $\mathbb R^4$ is a quotient of a finite-dimensional quaternionic vector space by a unitary group, and the equations that define the quotient are the vanishing of the three components of a quaternionic moment map. This is the one place in the topological programme where the biquaternion algebra is not a convenient packaging of a complex construction but the construction's native field.

The article proceeds in four steps. It writes the self-duality equation and identifies its quaternionic content; it states the ADHM equations and the quotient; it derives the dimension of the moduli space by counting the data, the constraints and the gauge redundancy, and checks the counting against the known cases; and it verifies the minimal ($k=1$) datum against the equations and against the BPST solution. It then separates the algebraic content from the analytic input, because the existence and completeness of the construction — that every self-dual connection arises this way and that the quotient is a manifold — are theorems of analysis, not identities of the algebra.

**Conventions.** We use those of *Conventions in the Biquaternion Universe* and of the companion gauge articles. The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ with $e_k^2=-e_0$, $e_1e_2=e_3$, and central $i$; the real-quaternion subspace is $\mathbb H_{\mathbb B}=\mathrm{span}_{\mathbb R}\{e_0,e_1,e_2,e_3\}$ and the compact factor is $SU(2)=\{U\in\mathbb H_{\mathbb B}:U\bar U=e_0\}$. On the Euclidean slice the coordinates are $x_4,x_1,x_2,x_3$ with the self-dual 't Hooft symbols $\eta^a_{\mu\nu}$ of *Instantons and Solitons in Biquaternionic Form*, and the curvature is written without the explicit factor of $i$ in the commutator, $F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+[\mathcal A_\mu,\mathcal A_\nu]$, on Hermitian generators with $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$; the placement of the factor $i$ is the signature convention recorded in that article. The matrix trace on the gauge factor is distinguished from the informational trace $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$.

- Companion article *Instantons and Solitons in Biquaternionic Form*, for the instanton solutions and the topological charge.
- Companion article *The Hopf Fibration and the Biquaternion Gauge Bundle*, for the boundary data and the structure group.
- Companion article *The Index Theorem and the Zero-Mode Count in Biquaternionic Form*, for the zero-mode count on the background.
- Companion article *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*, for the use of the moduli in the functional integral.

## Self-Duality as a Quaternionic Equation

The Hodge star on the Euclidean slice satisfies $\star^2=+1$ on two-forms, so its eigenvalues are $\pm1$ and every two-form splits into a self-dual and an anti-self-dual part,

$$
F=\underbrace{\tfrac12(F+\star F)}_{F^+}+\underbrace{\tfrac12(F-\star F)}_{F^-},
\qquad
\star F^\pm=\pm F^\pm .
$$

The self-duality equation is $F^-=0$, equivalently $F=\star F$, equivalently the three conditions

$$
F_{12}=F_{34},\qquad F_{13}=-F_{24},\qquad F_{14}=F_{23},
$$

in terms of which the six independent components are reduced to three. The companion article established that a solution of this first-order equation is automatically a solution of the second-order Yang–Mills equation, by the Bianchi identity, and that it saturates the Bogomolny bound $S\ge 8\pi^2|Q|/g^2$. What the present article adds is the recognition that the three conditions above are the three components of one quaternionic statement.

**The quaternionic structure.** Identify a point of $\mathbb R^4$ with a real quaternion,

$$
x \;=\; x_4\,e_0 + x_1\,e_1 + x_2\,e_2 + x_3\,e_3 \in\mathbb H_{\mathbb B} ,
$$

or, grouping the coordinates into two complex numbers, with a pair $(z_1,z_2)\in\mathbb C^2$ by $z_1=x_2+ix_1$, $z_2=x_4+ix_3$. Multiplication of quaternions is complex-linear in the second factor of $\mathbb B=\mathbb C\otimes\mathbb H$, so it makes $\mathbb C^2$ into a quaternionic line: right multiplication by $e_1,e_2,e_3$ generates an action of the quaternion units. The Hodge star acts on two-forms with $\star^2=+1$, and the rotation group of the Euclidean slice factors as $SU(2)_+\times SU(2)_-$ up to a central $\mathbb Z_2$, with $SU(2)_+$ acting on the self-dual two-forms as the triplet $\mathbf 3$ and as singlets on the anti-self-dual ones, and $SU(2)_-$ the other way round. A **self-dual** two-form is exactly the component that transforms as the triplet of $SU(2)_+$ and is a singlet of $SU(2)_-$: its three independent components are the three components of that triplet, and relative to a compatible complex structure they are the Kähler form together with the real and imaginary parts of a holomorphic two-form. This is the sense in which the instanton equation is quaternionic rather than merely four-dimensional.

The practical consequence is that the data of a self-dual connection, being quaternionic, should be parametrised by quaternionic linear algebra. That is the content of the ADHM theorem.

## The ADHM Equations

Let $k\ge1$ be the instanton number and let $N$ be the rank of the gauge group taken for the moment as $U(N)$ or $SU(N)$; for the framework $N=2$. Introduce the data

$$
B_1,B_2 \in \mathrm{End}(\mathbb C^k),
\qquad
I \in \mathrm{Hom}(\mathbb C^N,\mathbb C^k),
\qquad
J \in \mathrm{Hom}(\mathbb C^k,\mathbb C^N),
$$

so that $B_1,B_2$ are $k\times k$ complex matrices, $I$ is $k\times N$, and $J$ is $N\times k$. The ADHM equations are two equations, one real and one complex,

$$
\boxed{\;\mu_{\mathbb R}=[B_1,B_1^\dagger]+[B_2,B_2^\dagger]+I I^\dagger - J^\dagger J = 0\;}
\qquad\text{in }\mathfrak u(k),
$$

$$
\boxed{\;\mu_{\mathbb C}=[B_1,B_2]+I J=0\;}
\qquad\text{in }M_k(\mathbb C).
$$

The data are acted on by the unitary group $U(k)$,

$$
B_a\mapsto gB_ag^{-1},\qquad I\mapsto gI,\qquad J\mapsto Jg^{-1},\qquad g\in U(k),
$$

under which both equations are equivariant, and the moduli space is the quotient

$$
\mathcal M_k \;=\; \mu^{-1}(0)\big/ U(k),
\qquad
\mu=(\mu_{\mathbb R},\mu_{\mathbb C}) .
$$

The three real components of $\mu_{\mathbb R}$ and the complex equation $\mu_{\mathbb C}$ together have $k^2+2k^2=3k^2$ real components, which is the real dimension of $\mathfrak u(k)\otimes\mathrm{Im}\,\mathbb H$; this is why $\mu$ is the **quaternionic moment map** of the data. The quotient by the $U(k)$ action that preserves $\mu=0$ is the hyperkähler quotient, and it is the statement that the four equations are the components of one quaternionic equation that gives the construction its structure.

**The instanton data from the equations.** The theorem of Atiyah, Drinfeld, Hitchin and Manin is that there is a bijection

$$
\bigl\{\text{self-dual connections on }\mathbb R^4\text{ of charge }k\bigr\}\big/\text{gauge}
\;\longleftrightarrow\;
\mu^{-1}(0)/U(k),
$$

realised by an explicit linear-algebra construction: from the data one forms a matrix $\Delta(x)$, linear in the quaternionic coordinate $x$, whose kernel is the relevant space; a normalised basis $v(x)$ of that kernel gives the connection through

$$
\mathcal A_\mu \;=\; \bar v\,\partial_\mu v ,
$$

which is a pure-gauge-like expression in the $x$-dependent kernel; the self-duality of $\mathcal A$ is a consequence of the two ADHM equations, and a computation shows that the curvature is $F_{\mu\nu}=\bar v\,\tilde F_{\mu\nu}v$ with $\tilde F$ built from the data. The construction is the standard one and is cited rather than re-derived; its algebraic content is the pair of equations and the quotient, which are what the framework's quaternionic structure makes natural.

## The Dimension of the Moduli Space

The dimension of $\mathcal M_k$ follows from the counting of the data, the constraints and the gauge redundancy, and the counting is worth doing explicitly because it is the ADHM construction's sharpest quantitative statement.

**Data.** $B_1$ and $B_2$ are each $k\times k$ complex, contributing $4k^2$ real dimensions in total (each has $2k^2$). $I$ is $k\times N$ complex and $J$ is $N\times k$ complex, so together they have $2kN$ complex entries, or $4kN$ real. The total real dimension of the data space is therefore

$$
\dim_{\mathbb R}\bigl(\text{data}\bigr)=4k^2+4kN .
$$

**Constraints.** The complex equation $\mu_{\mathbb C}=0$ has $k^2$ complex components, or $2k^2$ real; the real equation $\mu_{\mathbb R}=0$ is an anti-Hermitian $\mathfrak u(k)$-valued condition with $k^2$ real components. The constraint surface therefore has real dimension

$$
\dim_{\mathbb R}\mu^{-1}(0)=4k^2+4kN-3k^2 = k^2+4kN .
$$

**Quotient.** The group $U(k)$ has real dimension $k^2$, and it acts freely on a dense open set of $\mu^{-1}(0)$ (the set of **irreducible** data, those for which no proper subspace is preserved by all the data). Hence

$$
\dim_{\mathbb R}\mathcal M_k = k^2+4kN - k^2 = 4kN .
$$

This agrees with the standard formula $\dim_{\mathbb R}\mathcal M_k=4k\,h^\vee$ for a simple group of dual Coxeter number $h^\vee$, since $h^\vee=N$ for $SU(N)$. For the framework's gauge factor $N=2$,

$$
\dim_{\mathbb R}\mathcal M_k = 8k ,
\qquad
\dim_{\mathbb R}\mathcal M_k^{\text{physical}} = 8k-3 ,
$$

the second after removing the three-dimensional global $SU(2)$ rotation that acts trivially on the physical configuration. Thus $k=1$ has the five moduli of the BPST solution — four translations and one dilatation — and $k=2$ has thirteen. The dimension count is a check on the construction, not a substitute for it: it says that the data can locally parametrise a space of the right size, and it fixes the count of collective coordinates that the semiclassical expansion integrates over.

## The Minimal Datum and the BPST Instanton

The simplest ADHM datum is the $k=1$, $N=2$ case, where $B_1$ and $B_2$ are scalars, $I$ is a row and $J$ a column. Write the scalars as zero and

$$
B_1=B_2=0,
\qquad
I=(\rho,\;0),
\qquad
J=\begin{pmatrix}0\\ \rho\end{pmatrix},
\qquad \rho>0 .
$$

The complex equation is satisfied identically,

$$
\mu_{\mathbb C}=[B_1,B_2]+IJ = 0 + (\rho,\;0)\begin{pmatrix}0\\ \rho\end{pmatrix}=0 ,
$$

and the real equation is satisfied by the equality of the two moduli,

$$
\mu_{\mathbb R}=II^\dagger - J^\dagger J = |\rho|^2 - |\rho|^2 = 0 ,
$$

both verified exactly. The single real parameter $\rho$ is the instanton scale. The construction applied to this datum yields the BPST configuration of the companion article,

$$
\mathcal A_\mu^a(x)=2\,\eta^a_{\mu\nu}\,\frac{x_\nu}{r^2+\rho^2} ,
$$

which that article verified to be self-dual and to satisfy the equation of motion. The five moduli of the physical $k=1$ solution are recovered as the four translations of the origin, which are not part of the ADHM data at all but appear in the reconstruction from $\Delta(x)$, and the scale $\rho$, which is the datum; the three global $SU(2)$ orientations are the quotient by the global symmetry. For $k>1$ the matrices $B_1,B_2$ carry the relative positions and orientations of the individual instantons, and their non-commutativity $[B_1,B_2]$ is what the complex equation constrains.

This is the point at which the ADHM data and the framework meet. The relative-position matrix $B_1+iB_2$ is a complex matrix; its commutator $[B_1,B_2]$, whose vanishing would make the data simultaneously diagonalisable and the instantons independent, is precisely the quantity that a single quaternion cannot carry as a scalar. The complex equation $[B_1,B_2]+IJ=0$ is the statement that the obstruction to independence is cancelled by the boundary vectors $I$ and $J$, and it is the algebraic origin of the interaction between instantons. The biquaternion algebra accommodates the $k=1$ datum as a single $\rho$ and accommodates each $B_a$ as a complex number; the $k>1$ data require the matrix algebra $M_k(\mathbb C)\subset M_k(\mathbb B)$, which is the enlarged carrier discussed in *Grand Unification and the Biquaternion Algebra Ceiling*.

## The Twistor Construction and the Quaternionic Geometry

The ADHM equations are the algebraic shadow of a holomorphic-geometric statement, and the statement is quaternionic. The twistor space of the compactified four-space $S^4$ is the complex projective three-space $\mathbb{CP}^3$, which fibres over $S^4$,

$$
\mathbb{CP}^1\;\hookrightarrow\;\mathbb{CP}^3\;\longrightarrow\;S^4 ,
$$

with fibre $\mathbb{CP}^1\cong S^2$ over each point. The fibre is the space of complex structures compatible with the quaternionic structure of $\mathbb H_{\mathbb B}$: a point of $S^4$ is a quaternionic line, and the complex structures of that line are a $\mathbb{CP}^1$. This is the geometric form of the statement that $\mathbb H_{\mathbb B}$ admits a sphere of complex structures, and it is why the self-duality condition can be a holomorphic condition.

The Penrose–Ward correspondence states that a self-dual connection on $S^4$ is equivalent to a holomorphic rank-two vector bundle $E$ on $\mathbb{CP}^3$, trivial on each real line, and that the instanton number is the second Chern number of $E$. The ADHM data are the algebraic description of $E$ as a **monad**, a three-term exact sequence of holomorphic bundles,

$$
0\;\longrightarrow\;\mathcal O(-1)^{\oplus k}\;\xrightarrow{\ \alpha\ }\;\mathcal O^{\oplus(2k+N)}\;\xrightarrow{\ \beta\ }\;\mathcal O(1)^{\oplus k}\;\longrightarrow\;0 ,
$$

with $\alpha$ linear in the twistor coordinate and $\beta$ linear in it as well. The composite $\beta\alpha=0$ is exactly the pair of ADHM equations, and the $U(k)$ quotient is the freedom in choosing the monad; the bundle $E=\ker\beta/\mathrm{im}\,\alpha$ is the physical object, and the instanton at a point of $\mathbb R^4$ is recovered by restricting $E$ to the corresponding twistor line. Thus the quotient of this article and the holomorphic bundle are two descriptions of the same self-dual connection.

Two features make the construction *native* to the framework's algebra. First, the fibre $\mathbb{CP}^1$ is the complex projectivisation of the quaternionic line, and the quaternionic line is precisely the defining module $S\cong\mathbb C^2$ of $\mathbb B\cong M_2(\mathbb C)$; the twistor fibration is therefore the projectivisation of the algebra's own module, not an auxiliary space. Second, the ADHM quotient is a **hyperkähler quotient**: the flat space of the data $B_1,B_2,I,J$ carries the three complex structures of the quaternions, the moment map is $(\mu_{\mathbb R},\mu_{\mathbb C})$, and the quotient by the level set at zero is again hyperkähler. Hyperkähler geometry is the differential geometry of the quaternionic structure, and the algebra's three imaginary units are the three complex structures. The moduli space of instantons is therefore a hyperkähler manifold whose complex structures are the algebra's, which is the deepest sense in which the ADHM construction is the framework's own. The construction and the correspondence are standard; the algebra's role is that its module and its imaginary units are the objects being projectivised and varied.

## The Biquaternion Reading

The ADHM construction uses three structures, and all three are the framework's.

- **The quaternionic line.** The identification $\mathbb R^4\cong\mathbb H_{\mathbb B}$ is the framework's Euclidean slice; the two complex coordinates $z_1,z_2$ are the two components of the defining module $S\cong\mathbb C^2$ of $\mathbb B\cong M_2(\mathbb C)$, and the quaternion units act on $S$ by right multiplication. The self-duality equation is the statement that the curvature is quaternionic-holomorphic, and the three self-dual components form the triplet $\mathfrak{su}(2)\subset\mathbb M_-$.
- **The moment map.** The ADHM equations are the vanishing of a moment map for the quaternionic action, with values in $\mathfrak u(k)\otimes\mathrm{Im}\,\mathbb H_{\mathbb B}$. The imaginary quaternions are the pure-imaginary, anti-Hermitian part of $\mathbb H_{\mathbb B}$, i.e. exactly $\mathfrak{su}(2)\subset\mathbb M_-$ in the framework's decomposition $\mathbb M_-=\mathbb R(ie_0)\oplus\mathfrak{su}(2)$. The three real ADHM equations are therefore $\mathfrak{su}(2)$-valued, and the complex one is the complexified combination.
- **The quotient.** The hyperkähler quotient by $U(k)$ is the quotient by the compact group that the framework identifies as the maximal compact subgroup of the algebra of $k\times k$ biquaternion matrices. For $k=1$ this is the $U(1)$ of the centre; for $k>1$ it is the unitary group of the enlarged carrier.

What is standard and imported is equally clear. The ADHM theorem itself — existence and completeness, the bijection between the quotient and the self-dual connections, the freeness of the $U(k)$ action on irreducible data, and the smoothness of the moduli space away from the reducible locus — is a theorem of analysis and algebraic geometry, cited here and not re-derived. The explicit form of the matrix $\Delta(x)$ and the proof that the reconstructed connection is self-dual are likewise standard. The physical identification of the instanton number with a tunnelling amplitude, and the semiclassical use of the moduli, belong to *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*. The framework's contribution is that the equation and its solution space are quaternionic-linear, and that the quaternion algebra of the construction is the real-quaternion subspace of $\mathbb B$ rather than an auxiliary device.

## Summary

The self-duality equation $F=\star F$ on the Euclidean slice is a quaternionic equation: with $\mathbb R^4\cong\mathbb H_{\mathbb B}$ and $SU(2)\times SU(2)$ acting by left and right quaternion multiplication, a self-dual curvature is quaternionic-holomorphic and its three independent components carry the adjoint of the compact factor $\mathfrak{su}(2)\subset\mathbb M_-$. The ADHM construction parametrises all self-dual connections of charge $k$ by matrices $B_1,B_2\in M_k(\mathbb C)$, $I\in M_{k\times N}(\mathbb C)$, $J\in M_{N\times k}(\mathbb C)$ satisfying the real and complex equations

$$
\mu_{\mathbb R}=[B_1,B_1^\dagger]+[B_2,B_2^\dagger]+II^\dagger-J^\dagger J=0 ,
\qquad
\mu_{\mathbb C}=[B_1,B_2]+IJ=0 ,
$$

modulo the $U(k)$ action. The equations are the vanishing of a quaternionic moment map, and the quotient is the hyperkähler quotient $\mathcal M_k=\mu^{-1}(0)/U(k)$.

Counting data, constraints and gauge redundancy gives $\dim_{\mathbb R}\mathcal M_k=8k$ in the framework's two-dimensional-module convention, with $\dim_{\mathbb R}\mathcal M_k^{\text{physical}}=8k-3$ after removing the global $SU(2)$; $k=1$ reproduces the five moduli of BPST. The minimal datum $B_1=B_2=0$, $I=(\rho,0)$, $J=(0,\rho)^T$ satisfies both ADHM equations exactly and reconstructs the BPST solution. The quaternionic line, the moment map and the quotient are the framework's own structures; the ADHM existence and completeness theorems and the reconstruction formula are standard results transcribed. The obstruction carried by the commutator $[B_1,B_2]$ is the interaction between instantons, and for $k>1$ it lives in the enlarged matrix carrier rather than in a single biquaternion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra, $\cong M_2(\mathbb C)$ |
| $\mathbb H_{\mathbb B}$ | Real-quaternion subspace; Euclidean slice $\mathbb R^4$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary |
| $x=x_4e_0+x_1e_1+x_2e_2+x_3e_3$ | Quaternionic coordinate |
| $z_1=x_2+ix_1,\ z_2=x_4+ix_3$ | Complex coordinates, defining module $\mathbb C^2$ |
| $k$ | Instanton number (topological charge $Q$) |
| $N$ | Rank parameter; $N=2$ for the framework's $SU(2)$ |
| $B_1,B_2\in\mathrm{End}(\mathbb C^k)$ | ADHM matrices |
| $I\in\mathrm{Hom}(\mathbb C^N,\mathbb C^k)$, $J\in\mathrm{Hom}(\mathbb C^k,\mathbb C^N)$ | ADHM boundary vectors |
| $\mu_{\mathbb R}=[B_1,B_1^\dagger]+[B_2,B_2^\dagger]+II^\dagger-J^\dagger J$ | Real (moment-map) ADHM equation |
| $\mu_{\mathbb C}=[B_1,B_2]+IJ$ | Complex ADHM equation |
| $\mathcal M_k=\mu^{-1}(0)/U(k)$ | Instanton moduli space (hyperkähler quotient) |
| $\dim_{\mathbb R}\mathcal M_k=8k$ | Moduli dimension; physical $8k-3$ |
| $\Delta(x)$ | ADHM linear operator; kernel gives the connection |
| $\mathcal A_\mu=\bar v\,\partial_\mu v$ | Reconstruction of the self-dual connection |
| $\eta^a_{\mu\nu}$ | Self-dual 't Hooft symbols |
| $\rho$ | Instanton scale; the $k=1$ datum |
| $T(R)$, defining module | Dynkin index $\tfrac12$; the two-dimensional simple module of $\mathbb B$ |

## Further Reading

- Michael F. Atiyah, Vladimir G. Drinfeld, Nigel J. Hitchin and Yuri I. Manin, "Construction of instantons", *Physics Letters A* 65 (1978) 185–187, for the original ADHM construction.
- Michael F. Atiyah, Nigel J. Hitchin and Isadore M. Singer, "Self-duality in four-dimensional Riemannian geometry", *Proceedings of the Royal Society A* 362 (1978) 425–461, for the moduli-space dimension, the moment-map formulation and the twistor correspondence.
- Nigel J. Hitchin, Anders Karlhede, Ulf Lindström and Martin Roček, "Hyperkähler metrics and supersymmetry", *Communications in Mathematical Physics* 108 (1987) 535–589, for the hyperkähler quotient construction of the ADHM moduli space.
- Simon K. Donaldson, "An application of gauge theory to four-dimensional topology", *Journal of Differential Geometry* 18 (1983) 279–315, for the analytic properties of the instanton moduli space used in the completeness statement.
- Michael F. Atiyah, *Geometry of Yang–Mills Fields* (Accademia Nazionale dei Lincei, 1979), for the instanton data and the twistor-theoretic viewpoint.
- David Tong, *Gauge Theory* (lecture notes, University of Cambridge, 2018), for a pedagogical derivation of the ADHM construction and the explicit reconstruction formula.
- Nicholas Manton and Paul Sutcliffe, *Topological Solitons* (Cambridge University Press, 2004), for the instanton moduli space, its dimension and its role in the semiclassical expansion.
- Sidney Coleman, "The uses of instantons", in *Aspects of Symmetry* (Cambridge University Press, 1985), for the physical reading of the instanton data and moduli.
- Mikio Nakahara, *Geometry, Topology and Physics* (CRC Press, 2nd ed. 2003), for the quaternionic structure of $\mathbb R^4$ and the self-duality equation.
- E. Corrigan, D. B. Fairlie, S. Templeton and P. Goddard, "A Green's function for the general self-dual gauge field", *Nuclear Physics B* 140 (1978) 31–44, for the explicit reconstruction of the connection from the ADHM data.
